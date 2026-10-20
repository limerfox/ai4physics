"""Проверка наличия итогового PDF в папке results.

Запуск из корня проекта: python -m pytest tests/ -q
"""
from pathlib import Path


def test_new_paper_pdf_exists():
    pdf_path = Path("results") / "new_paper.pdf"
    assert pdf_path.exists(), f"файл не найден: {pdf_path.resolve()}"
    assert pdf_path.is_file(), f"это не файл: {pdf_path.resolve()}"

    return 0