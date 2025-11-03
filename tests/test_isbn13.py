try:
    from src.isbn import normalize_isbn, is_valid_isbn13
except ModuleNotFoundError:
    from isbn import normalize_isbn, is_valid_isbn13

import pytest

@pytest.mark.parametrize("raw", [
    "9780306406157",
    "978-3-16-148410-0",
])
def test_isbn13_valid_samples(raw):
    assert is_valid_isbn13(normalize_isbn(raw)) is True

@pytest.mark.parametrize("raw", [
    "9780306406158",   # checksum malo
    "978030640615",    # 12
    "97803064061570",  # 14
    "978030640615A",   # carácter inválido
    "",                # vacío
])
def test_isbn13_invalid_partitions(raw):
    assert is_valid_isbn13(normalize_isbn(raw)) is False
