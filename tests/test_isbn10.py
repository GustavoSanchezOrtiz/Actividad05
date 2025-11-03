
try:
    from src.isbn import normalize_isbn, is_valid_isbn10
except ModuleNotFoundError:
    from isbn import normalize_isbn, is_valid_isbn10

import pytest

@pytest.mark.parametrize("raw", [
    "0-306-40615-2",   # clásico válido
    "0471958697",
    "0-8044-2957-X",   # válido con X final
    "0306406152",
])
def test_isbn10_valid_samples(raw):
    s = normalize_isbn(raw)
    assert is_valid_isbn10(s) is True

@pytest.mark.parametrize("raw", [
    "0306406153",      # checksum incorrecto
    "123456789",       # 9 dígitos
    "12345678901",     # 11 dígitos
    "12345X7890",      # X no al final
    "12345678A9",      # carácter inválido
    "",                # vacío
    "------",          # solo separadores
])
def test_isbn10_invalid_partitions(raw):
    s = normalize_isbn(raw)
    assert is_valid_isbn10(s) is False
