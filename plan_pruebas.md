# Plan de Pruebas – Validador ISBN

## 1. Objetivo
Validar funcionalmente y por criterios de caja blanca las funciones de `isbn.py`:
`normalize_isbn`, `is_valid_isbn10`, `is_valid_isbn13`, `detect_isbn`.

## 2. Alcance y supuestos
- Entradas con separadores `-` y espacios; salida en mayúsculas.
- `normalize_isbn` devuelve `""` si detecta caracteres inválidos; los validadores fallan en esos casos.
- Determinismo, sin dependencias externas.

## 3. Estrategia
- **Caja negra:** particiones válidas/ inválidas por longitud, caracteres y checksum (ISBN-10: %11==0, X solo final; ISBN-13: pesos 1/3 y %10==0).
- **Fronteras:** longitudes 9/10/11 (ISBN-10) y 12/13/14 (ISBN-13); vacío; solo separadores.
- **Caja blanca:** cubrir ramas de: longitud incorrecta, carácter inválido, ‘X’ final/ no final, checksum correcto/incorrecto.
- **Propiedades:** (1) idempotencia de `normalize_isbn`; (2) equivalencia de formatos (con y sin separadores).

## 4. Matriz de trazabilidad (fragmento)
| Regla | Partición/Frontera | Caso | Test |
|------|---------------------|------|------|
| ISBN-10 con ‘X’ final | Caja blanca | `0-8044-2957-X` | `test_isbn10_valid_samples` |
| ISBN-10 X no final | Partición inválida | `12345X7890` | `test_isbn10_invalid_partitions` |
| ISBN-13 pesos 1/3 | Checksum válido | `9780306406157` | `test_isbn13_valid_samples` |
| Normalización | Idempotencia | `978-0-306-40615-7` | `test_normalize_idempotencia` |

## 5. Métricas objetivo
- Cobertura **líneas ≥ 90%** y **branches ≥ 85%**. Gaps justificables en ramas de errores inalcanzables por diseño.

## 6. Criterios de salida
- Suite verde local y en CI.
- Cobertura alcanza umbrales o gaps justificados con evidencia.

## 7. Riesgos
- Falsos negativos por ISBN de ejemplo mal tipeados.
- Dependencia de estructura del repo (ruta de import).
