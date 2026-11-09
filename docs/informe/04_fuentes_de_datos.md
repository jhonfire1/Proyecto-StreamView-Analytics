# 4. Descripción de las fuentes de datos

## Archivos originales (`data/raw/`)
| Archivo | Registros | Columnas |
|---|---|---|
| `netflix_movies_detailed_up_to_2025.csv` | 16.000 | 18 |
| `netflix_tv_shows_detailed_up_to_2025.csv` | 16.000 | 16 |

Variables principales: identificador (`show_id`), tipo, título, director, reparto, país, fecha de incorporación, año de estreno, géneros, idioma, descripción, popularidad, cantidad de votos y calificación promedio. Solo las películas incluyen `budget` y `revenue`.

## Proceso de limpieza (`notebooks/01_limpieza_datos.ipynb`)
| Regla | Decisión | Por qué |
|---|---|---|
| Columnas `duration` y `rating` | Eliminadas | `duration` está vacía en películas y es constante en series; `rating` es una copia exacta de `vote_average`, no una clasificación por edad |
| Duplicados | 9 `show_id` repetidos en series; se conserva la primera ocurrencia | Cada registro debe representar un único contenido |
| Nulos de texto (director, reparto, país, géneros) | Se imputan como "Sin dato" | No perder títulos que sí tienen datos numéricos |
| Fechas | `date_added` convertida a tipo fecha | Poder ordenar, filtrar y graficar en el tiempo |
| Datos financieros | Presupuesto o ingresos menores a USD 1.000 (o en 0) se tratan como dato faltante, no como cero real | Evitar distorsionar el ROI con montos simbólicos |
| Variables derivadas | `decada` y `ROI = ingresos / presupuesto` (solo con datos confiables) | Habilitar el análisis financiero y temporal |

## Archivos limpios (`data/processed/`)
| Archivo | Registros | Columnas |
|---|---|---|
| `netflix_movies_cleaned.csv` | 16.000 | 21 |
| `netflix_tv_cleaned.csv` | 15.991 | 18 |

Son la **única fuente de datos** de ambos dashboards. El notebook 01 los regenera con el mismo contenido.

## Limitaciones de los datos
1. **Cobertura financiera parcial:** solo 3.523 de 16.000 películas (22,0%) tienen presupuesto e ingresos confiables; ninguna serie tiene datos financieros.
2. **Muestra estratificada:** hay exactamente 1.000 películas y 1.000 series por cada año de estreno entre 2010 y 2025 (991 series en 2025 tras eliminar duplicados). Los conteos por año no reflejan el tamaño real del catálogo.
3. **Popularidad no es consumo real:** es un índice relativo (TMDB), no reproducciones dentro de StreamView.
4. **Títulos sin votos:** 4.560 títulos (5,6% de las películas y 22,9% de las series) tienen 0 votos y calificación 0; esto significa "sin votos", no "mala calificación", y se excluye de los promedios.
5. **Campos multivalor:** `genres`, `country`, `cast` y `director` contienen varios valores separados por coma; los conteos por categoría suman más que el total de títulos.
6. **Valores sin dato:** director en 11.092 títulos, país en 2.261, reparto en 1.360 y géneros en 1.079; además la descripción es nula en 132 películas y 3.203 series (no imputada).
7. **No existe clasificación etaria:** la columna que parecía serlo era un duplicado de `vote_average`.
