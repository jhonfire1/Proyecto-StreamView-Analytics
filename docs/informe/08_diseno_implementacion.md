# 8. Diseño e implementación del dashboard interactivo

## 8.1 Audiencias y herramientas

La solución integra dos dashboards complementarios:

| Dashboard | Audiencia | Herramienta y justificación |
|---|---|---|
| Ejecutivo | Directorio y Gerencia General | Power BI permite presentar indicadores consolidados y visualizaciones del catálogo en una interfaz de consulta general. |
| Analítico | Gerencia de Contenidos y Adquisición | Streamlit, pandas y Plotly permiten explorar contenidos, aplicar filtros y reutilizar las variables financieras preparadas en el proyecto. |

Ambos dashboards utilizan los archivos limpios de `data/processed/`.
Cada herramienta consulta estas fuentes de forma independiente;
Streamlit no depende del archivo de Power BI.

## 8.2 Organización de la información

Power BI presenta la composición general del catálogo mediante
indicadores, distribución de películas y series, países, géneros,
visualización temporal y mapa de producciones.

Streamlit organiza el análisis en cinco pestañas:

| Pestaña | Contenido principal |
|---|---|
| Popularidad y calificación | Dispersión entre ambas variables, tamaño de puntos según votos y correlación de Spearman. |
| Géneros | Popularidad y calificación promedio por género, junto con un treemap de volumen. |
| Rankings | Contenidos mejor evaluados y directores y actores con mayor cantidad de títulos. |
| Países | Mapa de calificación o popularidad promedio, tablas y contexto sobre exclusiones. |
| Finanzas | Indicadores financieros, presupuesto frente a ingresos, ranking por ingresos y películas que cumplen el criterio de éxito con presupuesto reducido. |

La organización en pestañas separa preguntas analíticas y permite
consultar cada tema sin mostrar todos los gráficos simultáneamente.

## 8.3 Indicadores y criterios de cálculo

El dashboard ejecutivo incluye indicadores de cantidad de contenidos,
películas, series, países, idiomas y géneros, además de popularidad
y calificación promedio.

Streamlit presenta como indicadores generales:
- títulos filtrados;
- popularidad promedio;
- calificación promedio de títulos con votos;
- cantidad de títulos con votos.

En Finanzas se muestran presupuesto promedio, ingresos totales,
presupuesto total y razón agregada ingresos/presupuesto. Se añaden
la mediana y el promedio de las razones individuales por película.

La cobertura financiera se informa respecto de las películas
seleccionadas. Las series y los registros que no cumplen la regla
de inclusión no se utilizan en estos indicadores.

## 8.4 Filtros y mecanismos de interacción

Power BI dispone de filtros por tipo de contenido, rango de años
y género.

Streamlit permite filtrar por tipo, año de estreno, calificación,
género, país e idioma. Sus gráficos incorporan detalles emergentes
y las tablas permiten consultar resultados adicionales.

El mapa permite alternar entre calificación y popularidad.
Los rankings de mejor evaluados exigen al menos 50 votos; el mapa
utiliza un mínimo de cinco títulos con votos por país y las barras
por género un mínimo de 30.

No se incorpora clasificación etaria porque la variable disponible
con ese nombre no representaba una clasificación válida, decisión
documentada desde la preparación de datos.

## 8.5 Consistencia visual y mantenimiento

Las funciones de carga, separación de campos multivalor, formatos
y colores compartidos se centralizan en `src/utils.py`.

La paleta distingue películas (#E50914) y series (#1F77B4) de forma consistente entre notebooks, Streamlit y Power BI, tras la revisión y ajuste realizados en el cierre del proyecto.

Los títulos, leyendas y notas explican unidades, poblaciones,
escalas y criterios de inclusión. Las escalas logarítmicas se
identifican explícitamente y la dispersión financiera incorpora
una línea de ingresos iguales al presupuesto.

## 8.6 Optimización y comprobaciones

En esta etapa se reforzó el contexto de popularidad, se ajustó
el cálculo de calificaciones de directores y actores, se
diferenciaron las medidas financieras y se transparentaron las
exclusiones del mapa.

También se añadieron explicaciones sobre correlación y pertenencia
a múltiples géneros. La revisión de la narrativa mantiene estas
distinciones entre el notebook y el informe.

Se realizaron comprobaciones visuales de las pestañas modificadas,
de la selección de solo películas y solo series, y del estado sin
resultados. El alcance de las pruebas y los casos pendientes se
documentan en el apartado 9.7.