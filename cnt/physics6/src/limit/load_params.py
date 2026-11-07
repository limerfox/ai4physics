import json
import numpy as np
import pandas as pd
from pathlib import Path
from dataclasses import fields
from typing import Any
from .experiment import RunConfig, PointResult, RunResult

POINT_COLS = ("H", "max_relative_error", "status", "message")
KEY_COLS   = ["method", "m", "k", "x", "t_ref", "dps", "fit_last_n"]

TUPLE_FIELDS = {"H_values", "t_values"}   # поля-tuple в RunConfig

def _to_tuple(v: Any) -> tuple:
    if isinstance(v, tuple):
        return v
    if isinstance(v, list):
        return tuple(v)
    if isinstance(v, str):
        s = v.strip()
        if not s:
            return ()
        # поддерживаем и JSON ("[1,2]"), и разделитель ("1;2" / "1,2")
        if s.startswith("["):
            import json
            return tuple(json.loads(s))
        return tuple(float(x) for x in s.replace(";", ",").split(","))
    raise TypeError(f"cannot convert to tuple: {v!r}")

def _clean_record(rec: dict) -> dict:
    """Оставить только поля RunConfig, привести tuple-поля."""
    allowed = {f.name for f in fields(RunConfig)}
    out = {k: v for k, v in rec.items() if k in allowed}
    for name in TUPLE_FIELDS & out.keys():
        out[name] = _to_tuple(out[name])
    return out

def load_run_configs_json(out: Path) -> list[RunConfig]:
    path = Path(out) / "run_config.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [RunConfig(**_clean_record(rec)) for rec in raw]


def _py(v):
    if isinstance(v, np.integer):  return int(v)
    if isinstance(v, np.floating): return float(v)
    return v

def load_results(long_csv, summary_csv) -> list[RunResult]:
    df      = pd.read_csv(long_csv)
    summary = pd.read_csv(summary_csv)

    by_id  = summary.set_index("run_id").to_dict(orient="index")
    by_key = {tuple(_py(r[c]) for c in KEY_COLS): r
              for r in summary.to_dict(orient="records")}

    config_cols = [c for c in df.columns if c not in POINT_COLS]
    out: list[RunResult] = []

    for keys, g in df.groupby(config_cols, sort=False, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        rec = dict(zip(config_cols, keys))

        # H_values восстанавливаем из точек (в том порядке, что был в config)
        rec["H_values"] = tuple(float(h) for h in g["H"])
        config = RunConfig(**_clean_record(rec))

        points = tuple(
            PointResult(
                H=float(r.H),
                max_relative_error=float(r.max_relative_error),
                status=str(r.status),
                message="" if pd.isna(r.message) else str(r.message),
            )
            for r in g[list(POINT_COLS)].itertuples(index=False)
        )

        # сначала ищем по run_id, иначе — по ключу параметров
        s = by_id.get(config.run_id())
        if s is None:
            s = by_key.get(tuple(_py(rec[c]) for c in KEY_COLS), {})

        out.append(RunResult(
            config=config,
            points=points,
            p_estimate=float(s.get("p_estimate", float("nan"))),
            log_fit_rmse=float(s.get("log_fit_rmse", float("nan"))),
            n_valid=int(s.get("n_valid", sum(p.status == "ok" for p in points))),
        ))

    return out