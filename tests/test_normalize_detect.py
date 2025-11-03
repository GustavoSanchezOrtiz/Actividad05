try:
    from src.isbn import normalize_isbn, detect_isbn
except ModuleNotFoundError:
    from isbn import normalize_isbn, detect_isbn

def test_normalize_remueve_espacios_y_guiones():
    assert normalize_isbn(" 0-306-40615-2 ") == "0306406152"

def test_normalize_invalida_cadena_mala():
    # Tu normalize devuelve "" si hay caracteres prohibidos
    assert normalize_isbn("ABC-123") == ""

def test_detect_isbn10_y_isbn13():
    assert detect_isbn("0-8044-2957-X") == "ISBN-10"
    assert detect_isbn("978-3-16-148410-0") == "ISBN-13"
    assert detect_isbn("not-an-isbn") == "INVALID"
