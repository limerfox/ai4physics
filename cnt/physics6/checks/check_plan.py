import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.limit.load_params import load_run_configs_json

def check_plan():
    print("Проверка пробного прогона:")
    parser = argparse.ArgumentParser(description="Проверка первого шага: Пробный прогон.")
    parser.add_argument("--output", default="results", help="Выходной каталог.")
    args = parser.parse_args()

    out = Path(args.output)
    js = out / "run_config.json"
    configs = []
    if js.is_file() and js.stat().st_size > 0:
        configs = load_run_configs_json(out)

    set_id = set([config.run_id() for config in configs])
    # Проверка, что имена прогонов не повторяются
    assert len(set_id) == len(configs)
    print("Пробный прогон проверку прошел.")

check_plan()