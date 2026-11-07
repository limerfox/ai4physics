import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from checks_function.test_error_monotonically_decrease import test_error_monotonically_decrease
from checks_function.test_convergence_order import test_convergence_order
from checks_function.test_deterministic_result import test_deterministic_result

from src.limit.load_params import load_run_configs_json, load_results
from src.limit.experiment import run_many

def check():
    print("Проверка полного расчета:")
    parser = argparse.ArgumentParser(description="Проверка третьего шага: Полный расчет.")
    parser.add_argument("--output", default="results", help="Выходной каталог.")
    args = parser.parse_args()

    out = Path(args.output)
    js = out / "run_config.json"
    configs = []
    if js.is_file() and js.stat().st_size > 0:
        configs = load_run_configs_json(out)
    else:
        raise Exception("Запустить пробный прогон и проверку к нему")
    
    results = load_results(out / "runs.csv", out / "summary.csv")

    print("Результаты получены. Начинается проверка результатов на корректность.")
    print("Проверка на детерминированность результатов (исключая точки без статуса 'ok').")
    for config in configs:
        test_deterministic_result(config)
    
    print("Проверка на монотонное убывание ошибки (исключая сравнения точек без статуса 'ok') и порядок сходимости.")
    for result in results:
        test_error_monotonically_decrease(result)
        test_convergence_order(result)
    print("Полный расчет отработал корректно.")

check()