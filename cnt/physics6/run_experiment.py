#!/usr/bin/env python3
"""Main entry point for the de Sitter flat-limit experiment."""
import argparse
# import sys
import pandas as pd
import json

from src.limit.experiment import save_plan, run_many
from pathlib import Path
# ROOT = Path(__file__).resolve().parent
# sys.path.insert(0, str(ROOT / "src"))
from dataclasses import replace

from src.limit.experiment import run_experiment, METHODS
from src.limit.config import DEFAULT_H_VALUES, DEFAULT_M_VALUES, DEFAULT_K_VALUES, DEFAULT_T_VALUES

# from checks.test_error_monotonically_decrease import test_error_monotonically_decrease
# from checks.test_convergence_order import test_convergence_order
# from checks.test_deterministic_result import test_deterministic_result

def main():
    parser = argparse.ArgumentParser(description="Проверка плоского предела de Sitter -> Minkowski.")
    parser.add_argument("--output", default="results", help="Выходной каталог.")
    parser.add_argument("--dps", type=int, default=60, help="mpmath десятичная точность.")
    parser.add_argument("--plan", action="store_true", help="Пробный прогон: сборка плана, создание всех конфигураций для эксперимента.")
    args = parser.parse_args()

    kwargs = {"output_dir": args.output,
              "h_values": DEFAULT_H_VALUES,
              "m_values": DEFAULT_M_VALUES,
              "k_values": DEFAULT_K_VALUES,
              "t_values": DEFAULT_T_VALUES,
              "methods": tuple(METHODS),
              "dps": args.dps,
              "fit_last_n": 4,
              "x": 1.0,
              "t_ref": 1.0}

    if args.plan:
        out = Path(args.output)
        out.mkdir(parents=True, exist_ok=True)
    
        configs = save_plan(**kwargs)
    else:
        rows, summary = run_experiment(**kwargs)
        statuses = rows["status"].tolist()
        failed = sum(st != "ok" for st in statuses)
        print(f"Finished: {len(rows)} runs; failed points: {failed}")
        print(f"Results: {Path(args.output).resolve()}")

if __name__ == "__main__":
    main()
