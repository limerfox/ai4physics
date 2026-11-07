"""Планирование, выполнение и сводка прогонов проверки плоского предела.

Один RunConfig задаёт одну серию (method, m, k) на всей сетке H.
Это позволяет оценивать порядок сходимости по одной конфигурации, а не
смешивать точки с разными массами, импульсами или методами.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Iterable

import pandas as pd

from .asymptotic import wkb_first_order_mode
from .config import (
    DEFAULT_H_VALUES,
    DEFAULT_K_VALUES,
    DEFAULT_M_VALUES,
    DEFAULT_T_VALUES,
)
from .errors import error_curve, estimate_order
from .modes import desitter_mode_float64, desitter_mode_mpmath

METHODS = {
    "float64": desitter_mode_float64,
    "mpmath": desitter_mode_mpmath,
    "asymptotic": wkb_first_order_mode,
}


@dataclass(frozen=True)
class RunConfig:
    """Все параметры, от которых зависит одна серия результатов."""

    method: str = "mpmath"
    m: float = 1.0
    k: float = 1.0
    H_values: tuple[float, ...] = DEFAULT_H_VALUES
    t_values: tuple[float, ...] = DEFAULT_T_VALUES
    x: float = 0.0
    t_ref: float = 0.0
    dps: int = 80
    fit_last_n: int = 4

    def __post_init__(self):
        # Нормализуем списки/диапазоны, чтобы конфигурация была хешируемой.
        object.__setattr__(self, "H_values", tuple(float(v) for v in self.H_values))
        object.__setattr__(self, "t_values", tuple(float(v) for v in self.t_values))
        self.validate()

    def validate(self) -> None:
        if self.method not in METHODS:
            raise ValueError(f"Unknown method {self.method!r}; choose from {tuple(METHODS)}")
        if self.m <= 0 or self.k <= 0:
            raise ValueError("This implementation requires m > 0 and k > 0.")
        if not self.H_values or any(h <= 0 for h in self.H_values):
            raise ValueError("H_values must be a non-empty sequence of positive values.")
        if len(set(self.H_values)) != len(self.H_values):
            raise ValueError("H_values must not contain duplicates.")
        if any(a <= b for a, b in zip(self.H_values, self.H_values[1:])):
            raise ValueError("H_values must be ordered strictly from large to small.")
        if not self.t_values:
            raise ValueError("t_values must not be empty.")
        if self.dps < 30:
            raise ValueError("Use at least 30 decimal digits for mpmath.")
        if self.fit_last_n < 2:
            raise ValueError("fit_last_n must be at least 2.")

    def run_id(self) -> str:
        """Одинаковая конфигурация — одинаковое имя, при любом порядке запуска."""
        return hashlib.sha1(repr(sorted(asdict(self).items())).encode()).hexdigest()[:8]

    def name(self) -> str:
        return (
            f"{self.method}_m{self.m:g}_k{self.k:g}_"
            f"{self.run_id()}"
        )

    def hparams(self) -> dict[str, float | int | str]:
        """Compact configuration fields suitable for the results table."""
        return {
            "method": self.method,
            "m": self.m,
            "k": self.k,
            "n_H": len(self.H_values),
            "H_max": max(self.H_values),
            "H_min": min(self.H_values),
            "n_t": len(self.t_values),
            "x": self.x,
            "t_ref": self.t_ref,
            "dps": self.dps,
            "fit_last_n": self.fit_last_n,
            "run_id": self.run_id(),
            "run": self.name(),
        }


@dataclass(frozen=True)
class PointResult:
    """Результат вычисления ошибки при одном значении H."""

    H: float
    max_relative_error: float
    status: str = "ok"
    message: str = ""


@dataclass(frozen=True)
class RunResult:
    """Результат одной серии на всей сетке H."""

    config: RunConfig
    points: tuple[PointResult, ...]
    p_estimate: float
    log_fit_rmse: float
    n_valid: int


def grid(base: RunConfig, **axes: Iterable) -> list[RunConfig]:
    """Сгенерировать декартово произведение параметров.

    Например: grid(base, method=METHODS, m=(0.5, 1.0), k=(1.0, 2.0)).
    Параметры, не указанные в axes, остаются из base.
    """
    unknown = set(axes) - set(RunConfig.__dataclass_fields__)
    if unknown:
        raise ValueError(f"Unknown RunConfig fields: {sorted(unknown)}")
    names = list(axes)
    if not names:
        return [base]
    values = [tuple(axes[name]) for name in names]
    if any(not axis for axis in values):
        raise ValueError("Every grid axis must contain at least one value.")
    configs = [
        replace(base, **dict(zip(names, combination)))
        for combination in itertools.product(*values)
    ]
    ids = [config.run_id() for config in configs]
    if len(ids) != len(set(ids)):
        raise RuntimeError("Grid generated duplicate run IDs.")
    return configs


def run(config: RunConfig) -> RunResult:
    """Выполнить одну конфигурацию; сбой отдельного H не теряет всю серию."""
    config.validate()
    mode_function = METHODS[config.method]
    point_results: list[PointResult] = []

    for H in config.H_values:
        try:
            kwargs = {"dps": config.dps} if config.method == "mpmath" else {}
            error = error_curve(
                mode_function,
                [H],
                config.m,
                config.k,
                config.t_values,
                x=config.x,
                t_ref=config.t_ref,
                **kwargs,
            )[0]
            if not math.isfinite(error):
                raise ArithmeticError("Non-finite relative error.")
            point_results.append(PointResult(float(H), float(error)))
        except Exception as exc:  # сохраняем ошибку точки и продолжаем серию
            point_results.append(
                PointResult(float(H), float("nan"), "failed", f"{type(exc).__name__}: {exc}")
            )

    valid = [p for p in point_results if p.status == "ok"]
    valid_H = [p.H for p in valid]
    valid_errors = [p.max_relative_error for p in valid]
    p, fit_rmse = estimate_order(valid_H, valid_errors, last_n=config.fit_last_n)
    return RunResult(config, tuple(point_results), p, fit_rmse, len(valid))


def run_many(configs: Iterable[RunConfig]) -> list[RunResult]:
    """Последовательно выполнить план прогонов в заданном порядке."""
    return [run(config) for config in configs]


def results_table(results: list[RunResult]) -> pd.DataFrame:
    """Длинная таблица: одна строка на пару (конфигурация, H)."""
    rows = []
    for result in results:
        row_base = result.config.hparams()
        for point in result.points:
            rows.append({
                **row_base,
                "H": point.H,
                "max_relative_error": point.max_relative_error,
                "status": point.status,
                "message": point.message,
            })
    return pd.DataFrame(rows)


def summary_table(results: list[RunResult]) -> pd.DataFrame:
    """Краткая таблица: одна строка на серию (method, m, k)."""
    rows = []
    for result in results:
        rows.append({
            **result.config.hparams(),
            "p_estimate": result.p_estimate,
            "log_fit_rmse": result.log_fit_rmse,
            "n_valid": result.n_valid,
        })
    return pd.DataFrame(rows)


def build_plan(
    h_values=DEFAULT_H_VALUES,
    m_values=DEFAULT_M_VALUES,
    k_values=DEFAULT_K_VALUES,
    t_values=DEFAULT_T_VALUES,
    methods=tuple(METHODS),
    dps: int = 80,
    fit_last_n: int = 4,
    x: float = 0.0,
    t_ref: float = 0.0,
) -> list[RunConfig]:
    """Создать полный план до начала вычислений."""
    base = RunConfig(
        H_values=tuple(h_values), t_values=tuple(t_values), dps=dps,
        fit_last_n=fit_last_n, x=x, t_ref=t_ref,
    )
    return grid(base, method=methods, m=m_values, k=k_values)

def save_plan(
    output_dir="results",
    h_values=DEFAULT_H_VALUES,
    m_values=DEFAULT_M_VALUES,
    k_values=DEFAULT_K_VALUES,
    t_values=DEFAULT_T_VALUES,
    methods=tuple(METHODS),
    dps: int = 80,
    fit_last_n: int = 4,
    x: float = 0.0,
    t_ref: float = 0.0,
) -> list[RunConfig]:
    """Сохранить созданный полный план."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    configs = build_plan(
        h_values=h_values,
        m_values=m_values,
        k_values=k_values,
        t_values=t_values,
        methods=methods,
        dps=dps,
        fit_last_n=fit_last_n,
        x=x,
        t_ref=t_ref,
    )
    if not configs:
        raise ValueError("The experiment plan is empty.")

    # Сначала фиксируем план. Даже если вычисление прервётся, останется
    # точное описание того, что собирались запускать.
    plan = [asdict(config) | {"run_id": config.run_id(), "name": config.name()}
            for config in configs]
    (out / "run_config.json").write_text(
        json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    pd.DataFrame([config.hparams() for config in configs]).to_csv(
        out / "run_plan.csv", index=False
    )
    return configs

def run_experiment(
    output_dir="results",
    h_values=DEFAULT_H_VALUES,
    m_values=DEFAULT_M_VALUES,
    k_values=DEFAULT_K_VALUES,
    t_values=DEFAULT_T_VALUES,
    methods=tuple(METHODS),
    dps=80,
    fit_last_n=4,
    x: float = 0.0,
    t_ref: float = 0.0,
):
    """Построить план, сохранить его до запуска, выполнить и записать результаты.

    Возвращает (runs_df, summary_df), сохраняя совместимость с главным скриптом.
    """
    out = Path(output_dir)
    configs = save_plan(output_dir, h_values, m_values, k_values, t_values, methods, dps, fit_last_n, x, t_ref)
    results = run_many(configs)
    runs_df = results_table(results)
    summary_df = summary_table(results)
    runs_df.to_csv(out / "runs.csv", index=False)
    summary_df.to_csv(out / "summary.csv", index=False)
    return runs_df, summary_df
