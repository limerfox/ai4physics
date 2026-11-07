import argparse
import sys
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from checks_function.test_error_monotonically_decrease import test_error_monotonically_decrease
from checks_function.test_convergence_order import test_convergence_order
from checks_function.test_deterministic_result import test_deterministic_result

from src.limit.load_params import load_run_configs_json
from src.limit.experiment import run_many, METHODS
from src.limit.config import DEFAULT_T_VALUES

def check_quick():
    print("Выполнение короткой проверки:")
    parser = argparse.ArgumentParser(description="Проверка второго шага: Короткая проверка.")
    parser.add_argument("--output", default="results", help="Выходной каталог.")
    args = parser.parse_args()

    out = Path(args.output)
    js = out / "run_config.json"
    configs = []
    if js.is_file() and js.stat().st_size > 0:
        configs = load_run_configs_json(out)
    else:
        raise Exception("Запустить пробный прогон и проверку к нему")

    quick_configs = [replace(configs[0], method=method, t_values=[DEFAULT_T_VALUES[0]]) for method in METHODS]
    results = run_many(quick_configs)
    print("Результаты получены. Начинается проверка результатов на корректность.")
    for config in quick_configs:
        test_deterministic_result(config)
    for result in results:
        test_error_monotonically_decrease(result)
        test_convergence_order(result)
    print("Короткая проверка отработала корректно.")

check_quick()