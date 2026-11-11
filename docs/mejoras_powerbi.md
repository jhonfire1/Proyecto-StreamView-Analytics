# Revisiones y mejoras para Power BI — Traspaso de Persona 2

## Alcance

Se conserva el dashboard ejecutivo aprobado en la experiencia
anterior. Las siguientes indicaciones buscan mantener coherencia
con la narrativa y las mejoras de comunicación de esta etapa.

La Persona 2 no modificó ni revalidó directamente el archivo
de Power BI. Por tanto, cada punto debe revisarse antes de decidir
si requiere un cambio.

## Lista de revisión

| ID | Elemento | Revisión o ajuste solicitado | Criterio de aceptación |
|---|---|---|---|
| BI01 | Paleta | Comprobar películas en rojo `#E50914` y series en azul `#1F77B4`. Ajustar únicamente si difiere de la paleta acordada. | El significado de los colores coincide con notebooks y Streamlit. |
| BI02 | Popularidad | Si se muestra este indicador, añadir o conservar una nota que lo identifique como índice relativo de TMDB, no reproducciones ni engagement. | La definición está disponible y la narrativa mantiene esa distinción. |
| BI03 | Calificación | Revisar el tratamiento de títulos sin votos. Para mantener la regla del indicador general de Streamlit, calcular la calificación sobre títulos con votos o explicar una diferencia intencional. | La población utilizada queda documentada y el resultado se contrasta con la fuente. |
| BI04 | Visualización temporal | Comprobar si utiliza año de estreno o fecha de incorporación. Ajustar título y nota para no presentar los conteos de la extracción como crecimiento real. | El gráfico identifica la variable temporal y el alcance del conjunto. |
| BI05 | Países y géneros | Aclarar que un título puede pertenecer a varias categorías cuando el conteo las desglosa. | No se interpreta la suma de categorías como total de títulos únicos. |
| BI06 | Mapa | Comprobar países representados, valores desconocidos y posibles omisiones. No trasladar automáticamente las cifras del mapa de Streamlit, porque sus criterios pueden ser distintos. | Las exclusiones y el significado de los valores no representados quedan explicados. |
| BI07 | Filtros y títulos | Verificar años, género y tipo de contenido; revisar que los títulos describan lo mostrado sin atribuir demanda o consumo. | Los indicadores responden a los filtros y los textos son coherentes. |
| BI08 | Fuentes | Comprobar que el dashboard utiliza los CSV entregados en `data/processed/` y documentar el cambio de origen si corresponde. | El archivo abre y puede actualizarse siguiendo el README. |

## Registro del resultado

Para cada punto, indicar uno de estos estados:

- Verificado sin cambios.
- Ajustado y comprobado.
- No aplica, con justificación.
- Pendiente, con motivo.

Registrar los cambios efectivos y guardar capturas cuando aporten
evidencia. No presentar una revisión sin cambios como una mejora
implementada.

## Coherencia con el informe

Si cambia una definición o un resultado de Power BI, revisar
las secciones del informe y la presentación que lo utilicen.

No es necesario agregar el bloque financiero de Streamlit al
dashboard ejecutivo únicamente para igualar ambas herramientas:
cada una mantiene su propósito y audiencia.