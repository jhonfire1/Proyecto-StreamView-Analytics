# 5. Análisis exploratorio mediante visualizaciones

Fuente: `notebooks/02_Visualizacion.ipynb` (8 gráficos). Cifras verificadas sobre `data/processed/`.


## Gráfico 1: Distribución películas vs series
El catálogo está equilibrado: **16.000 películas y 15.991 series (≈ 50% y 50%)**. Ningún formato domina en volumen, por lo que cualquier diferencia entre ellos debe buscarse en otras variables (popularidad, calificación, rentabilidad).

## Gráfico 2: Géneros predominantes (treemap)
Hay 29 géneros distintos, pero con fuerte concentración: **Drama (14.773 títulos)**, Comedy (9.106), Animation (4.070), Thriller (3.769) y Action (3.239). Un título puede tener varios géneros, por eso los conteos suman más que el total.

## Gráfico 3: Países e idiomas (top 10)
Hay 148 países y 83 idiomas, pero la concentración es aún mayor: **Estados Unidos aparece en 10.955 títulos**, seguido de Japón (2.869), Reino Unido (2.608), China (2.399) y Corea del Sur (2.174). El inglés domina con 13.969 títulos, seguido de chino (2.834), japonés (2.784), coreano (2.240) y español (1.646).

## Gráfico 4: Comparativa de popularidad (boxplot, escala log)
La mediana de popularidad de las **series (36,2) es unas 3 veces la de las películas (10,9)**. Precaución: la popularidad es un índice TMDB (no consumo en StreamView) y el 22,9% de las series tiene 0 votos frente al 5,6% de las películas; no debe leerse como causa directa de "más enganche".

## Gráfico 5: Popularidad vs calificación (dispersión)
Sobre los 27.431 títulos con votos, la correlación de Spearman es de **0,32**: positiva pero débil. Hay títulos muy bien calificados con baja popularidad y viceversa, por lo que "mejor evaluado" y "más popular" son fenómenos relacionados pero distintos. La calificación promedio es 7,02 en series y 6,31 en películas.

## Gráfico 6: Evolución de lanzamientos por año
Las líneas son **planas (1.000 por año y por formato)**. No es una tendencia real: es consecuencia de cómo se construyó la muestra (ver sección 4). Este gráfico no permite concluir crecimiento ni caída del catálogo.

## Gráfico 7: Presupuesto vs ingresos (solo películas con datos financieros)
Sobre 3.523 películas, los presupuestos van de USD 2.000 a USD 460 millones y los ingresos llegan a USD 2.799 millones. Con ejes logarítmicos, los puntos sobre la línea punteada ganaron más de lo que costaron. El ROI agregado (ingresos totales ÷ presupuestos totales) es **2,92x**, pero la mediana por película es **1,70x** y el promedio 4,29x: pocos casos extremos (máximo 559x) inflan el promedio.

## Gráfico 8: Éxito comercial según ROI (anillo)
- **36,6%** de las películas con datos financieros **no recuperó su inversión** (ROI < 1; 1.289 películas)
- **31,5%** tuvo un éxito moderado (ROI entre 1 y 3; 1.109 películas)
- **31,9%** tuvo un gran éxito (ROI mayor a 3; 1.125 películas)

Estos resultados aplican solo al 22,0% de las películas con datos financieros confiables.

## Síntesis
El catálogo es equilibrado en formatos pero **muy concentrado en pocos géneros, países e idiomas**. La rentabilidad es heterogénea: cerca de un tercio de las películas con datos multiplicó su inversión por 3 o más, y otro tercio no la recuperó.
