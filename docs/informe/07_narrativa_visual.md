# 7. Desarrollo de la narrativa visual

La narrativa se dirige al Directorio, la Gerencia General y la
Gerencia de Contenidos y Adquisición. Su mensaje central es que
la composición del catálogo, la popularidad, la valoración y los
indicadores financieros deben analizarse conjuntamente, sin
considerarlos medidas equivalentes de éxito.

## 7.1 ¿Qué está ocurriendo?

El catálogo analizado contiene 31.991 títulos: 16.000 películas
y 15.991 series. Aunque ambos formatos tienen una presencia
similar, sus indicadores de popularidad y valoración difieren.

En la selección general, la popularidad promedio es 20,4 para
películas y 64,9 para series. La calificación promedio de los
títulos con votos es 6,31 y 7,02, respectivamente. El boxplot
complementa estos promedios al mostrar diferencias de distribución
y valores extremos.

Estas diferencias describen los títulos analizados; no demuestran
que las series generen más reproducciones o engagement en StreamView.

Apoyo visual: distribución de películas y series, boxplot de
popularidad e indicadores segmentados por tipo de contenido.

La oferta también presenta concentración por categorías:
Drama, Comedy y Animation destacan entre los géneros, mientras
Estados Unidos encabeza el conteo por país asociado a la producción.
Estos resultados describen presencia en el catálogo, no demanda
ni ubicación de los espectadores.

## 7.2 ¿Por qué ocurre?

Los datos permiten explorar diferencias entre contenidos,
pero no establecer las causas de su popularidad o valoración.
Por ello, se revisan género, país y cantidad de votos como
dimensiones de comparación, no como explicaciones causales
confirmadas.

La disponibilidad de evaluaciones también difiere: aproximadamente
el 5,6 % de las películas y el 22,9 % de las series no tiene votos.
Estos registros no deben interpretarse como contenidos mal
evaluados y deben distinguirse al comparar calificaciones.

La popularidad es un índice relativo de TMDB, no una medida de
consumo dentro de StreamView. La ausencia de votos limita la
interpretación de las calificaciones, pero no demuestra por sí
sola la causa de las diferencias de popularidad.

Apoyo visual: popularidad y calificación por género, dispersión
de popularidad frente a calificación y cantidad de títulos con votos.

## 7.3 ¿Qué evidencia lo demuestra?

En la selección general, la correlación de Spearman entre
popularidad y calificación es 0,32, calculada sobre 27.431 títulos
con votos y datos en ambas variables. El resultado describe una
asociación, no una relación causal ni equivalencia entre popularidad
y valoración.

En finanzas, 3.523 películas cumplen los criterios de inclusión,
equivalentes al 22,0 % de las películas. La razón agregada
ingresos/presupuesto es 2,92x, mientras el promedio individual
es 4,29x y la mediana individual 1,70x. La diferencia entre promedio
y mediana muestra la importancia de no resumir los resultados
únicamente mediante el promedio.

Además, 1.289 de esas películas, correspondientes al 36,6 %, tienen
ingresos informados inferiores al presupuesto de producción
informado. Estos resultados describen únicamente el subconjunto
financiero y no representan beneficio neto ni rentabilidad de
StreamView.

Apoyo visual: dispersión con correlación, tarjetas financieras y
dispersión de presupuesto frente a ingresos con línea de referencia.

## 7.4 ¿Qué decisiones deben tomarse?

Se propone:

- Evaluar candidatos de adquisición combinando popularidad,
  calificación y cantidad de votos, sin priorizar automáticamente
  las series por su mayor popularidad promedio.
- Utilizar las comparaciones por género y país para identificar
  segmentos que requieren revisión, no como evidencia suficiente
  de demanda o de oportunidades comerciales confirmadas.
- Revisar las películas destacadas por sus indicadores financieros
  considerando cobertura, presupuesto y razones individuales,
  sin generalizar los resultados al catálogo completo.
- Comunicar a cada audiencia las limitaciones de los indicadores
  y mantener consistentes las definiciones entre dashboards,
  notebooks e informe.

Estas acciones orientan una evaluación posterior de contenidos;
los datos disponibles no permiten garantizar el resultado comercial
de una adquisición o campaña.

## 7.5 Cierre de la narrativa

La solución permite pasar de una descripción del catálogo a una
exploración de contenidos que merecen revisión. Su aporte consiste
en integrar evidencia y hacer explícitos sus límites, evitando
confundir presencia con demanda, popularidad con consumo o
ingresos con beneficio neto.