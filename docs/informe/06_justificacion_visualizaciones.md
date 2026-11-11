# 6. Justificación de las representaciones gráficas

Las representaciones se seleccionan según la pregunta analítica,
el tipo de variable y la audiencia. El dashboard ejecutivo prioriza
una lectura general del catálogo, mientras el analítico permite
explorar distribuciones, relaciones y resultados financieros.

| Representación | Aplicación y justificación | Alternativa considerada y limitación |
|---|---|---|
| Barras | Comparan cantidades o promedios entre categorías, como países, géneros y rankings. Su orientación horizontal facilita leer nombres largos y ordenar resultados. | Frente a un gráfico circular, permiten comparar con mayor claridad numerosas categorías. Los rankings deben indicar su alcance y criterios de inclusión. |
| Treemap | Presenta la composición por género mediante áreas proporcionales al volumen de títulos y permite reconocer categorías predominantes. | Las barras son preferibles para comparar valores cercanos con precisión. En el treemap, las categorías pequeñas requieren apoyo del detalle interactivo. |
| Boxplot | Compara la distribución de popularidad entre películas y series mediante mediana, dispersión y valores extremos. La escala logarítmica permite representar valores de magnitudes diferentes. | Una barra de promedios ocultaría la dispersión y los valores extremos. El boxplot describe diferencias en el índice TMDB, pero no demuestra mayor consumo ni engagement. |
| Dispersión | Explora asociaciones entre popularidad y calificación, y entre presupuesto e ingresos. En Streamlit, tamaño y color añaden contexto sobre votos y tipo de contenido. | Una línea no es adecuada para conectar títulos independientes. La superposición de puntos puede dificultar la lectura y una asociación no demuestra causalidad. |
| Líneas | Organizan los conteos por año de estreno y permiten seguir su secuencia temporal. | Las columnas también permiten comparar años individuales. En este conjunto, la distribución aproximadamente uniforme limita cualquier interpretación de crecimiento real del catálogo. |
| Mapa coroplético | Aporta contexto geográfico a la distribución o a los indicadores por país, según el dashboard. | Las barras permiten comparar países con mayor precisión. El mapa debe explicar su cobertura y no confundir ausencia de representación con un valor cero. |

## Criterios complementarios

- Escalas: el boxplot de popularidad y la dispersión financiera
  utilizan escalas logarítmicas identificadas para representar
  valores de magnitudes diferentes. En la dispersión financiera,
  la línea de ingresos iguales al presupuesto aporta una
  referencia adicional para interpretar cada título.
- Color: se mantiene una paleta compartida para películas y series.
  Las escalas continuas representan magnitudes y deben interpretarse
  mediante sus leyendas.
- Contexto: las notas explicitan cobertura financiera, cantidad de
  votos, poblaciones utilizadas y pertenencia a múltiples categorías.
- Interacción: los filtros y detalles emergentes permiten explorar
  la información sin añadir permanentemente todas las etiquetas.

Estas decisiones buscan facilitar la interpretación y apoyar
preguntas de negocio, sin atribuir a las visualizaciones conclusiones
que excedan el alcance de los datos.

## Relación con las decisiones de negocio

Las barras y el treemap permiten reconocer la composición del
catálogo y orientar la revisión de categorías. Las dispersiones
apoyan la exploración de relaciones entre indicadores y la
identificación de títulos que requieren análisis adicional.

El mapa aporta contexto sobre los países asociados a las
producciones, sin representar demanda ni ubicación de los usuarios.
La visualización temporal describe los años de estreno de los
títulos analizados, sin demostrar por sí sola la evolución histórica
del catálogo.

Las visualizaciones apoyan la exploración y priorización de
análisis; no sustituyen la evaluación comercial necesaria para
decidir una adquisición.