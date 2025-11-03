# Validador de ISBN (Python)

Valida ISBN-10 e ISBN-13 y detecta el tipo a partir de una cadena con o sin separadores.

## Requisitos
- Python 3.11+ (probado en 3.12)
- `pytest` y `coverage`

## Instalación
```bash
python -m pip install -U pip
pip install pytest coverage

## Pruebas de covertura
coverage run --branch -m pytest -q
coverage html
coverage xml
