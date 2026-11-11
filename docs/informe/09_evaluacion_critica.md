# 9. Evaluación crítica de la solución

## 9.1 Objetivo y alcance

La evaluación crítica tiene como propósito analizar la efectividad
de la solución de visualización desarrollada en las experiencias
anteriores e identificar oportunidades para fortalecer su claridad,
interpretación y utilidad para la toma de decisiones.

Se toma como punto de partida la solución previamente aprobada.
La revisión no busca reconstruir las funcionalidades existentes,
sino reconocer sus fortalezas, explicitar sus limitaciones y
justificar oportunidades de optimización.

La evaluación considera el diseño documentado del dashboard ejecutivo
de Power BI, el dashboard analítico de Streamlit y las visualizaciones
de la narrativa. La inspección de código y las comprobaciones de
ejecución de esta etapa se concentraron en Streamlit y en el notebook
de storytelling; no se realizó una nueva validación directa del archivo
de Power BI.

Se aplica el marco de cinco pasos del material
“3.3.1 Evaluación Crítica de las Visualizaciones”:
comprender el objetivo, revisar los datos, evaluar la representación,
analizar la interpretación y proponer mejoras.

Se distingue entre:
- funcionalidades y fortalezas existentes;
- limitaciones de los datos;
- oportunidades de mejora;
- cambios efectivamente implementados y comprobados.

## 9.2 Aplicación del marco de evaluación



### 9.2.1 Comprender el objetivo

La solución de StreamView Analytics tiene como objetivo transformar
la información del catálogo audiovisual en visualizaciones que
faciliten su exploración y apoyen decisiones relacionadas con la
composición del catálogo, la evaluación de contenidos y la
identificación de oportunidades de adquisición.

Para evaluar su pertinencia, se distinguen dos audiencias principales:

| Dashboard | Audiencia | Propósito | Decisiones que busca apoyar |
|---|---|---|---|
| Ejecutivo en Power BI | Directorio y Gerencia General | Entregar una visión consolidada de la composición del catálogo mediante indicadores y visualizaciones generales. | Orientar la revisión del portafolio según tipo de contenido, género, país y periodo analizado. |
| Analítico en Streamlit | Gerencia de Contenidos y Adquisición | Permitir una exploración detallada de popularidad, calificación, géneros, países y resultados financieros de películas con información disponible. | Identificar títulos y segmentos que requieren una revisión más profunda para apoyar decisiones de adquisición y posicionamiento. |

La evaluación considera si los indicadores y visualizaciones
contribuyen a estos propósitos y si su interpretación se mantiene
dentro del alcance de las fuentes disponibles.

La popularidad y la valoración permiten comparar características
de los contenidos, pero no deben interpretarse como medidas
directas de reproducciones, retención o comportamiento de los
suscriptores.

Asimismo, el análisis financiero se limita a películas que cumplen
los criterios de disponibilidad de presupuesto e ingresos definidos
en el proyecto. No corresponde extender sus resultados financieros
a las series ni a contenidos sin dicha información.

### 9.2.2 Revisar los datos

El proyecto utiliza los conjuntos de películas y series proporcionados
para StreamView Analytics. Según la documentación de preparación,
los datos procesados contienen 16.000 películas y 15.991 series,
con años de estreno entre 2010 y 2025.

Las fuentes permiten analizar la composición del catálogo,
popularidad, valoración y resultados financieros disponibles.
Su interpretación considera las siguientes limitaciones:

- Popularidad: es un índice relativo de TMDB, no una medida de
  reproducciones, engagement o retención.
- Calificación: debe analizarse junto con la cantidad de votos.
  Los títulos sin votos no equivalen a contenidos mal evaluados.
- Evaluaciones disponibles: en la selección general se muestran
  27.431 títulos con votos de un total de 31.991; la diferencia es
  de 4.560 títulos sin votos.
- Finanzas: el análisis incluye únicamente películas que cumplen
  la regla de presupuesto e ingresos del proyecto, con una cobertura
  aproximada del 22 % de las películas. Sus resultados no deben
  generalizarse a todo el catálogo ni a las series.
- Países y géneros: un título puede pertenecer a varias categorías,
  por lo que sus conteos no siempre suman el total de títulos únicos.
- Temporalidad: la distribución aproximadamente uniforme reportada
  por año no permite concluir que exista crecimiento o estabilidad
  real del catálogo.

En conclusión, los datos son pertinentes para los objetivos
descriptivos del proyecto, siempre que se expliciten su cobertura,
las reglas de inclusión y los límites de las conclusiones.
### 9.2.3 Evaluar la representación

Se revisan los tipos de gráficos, escalas, etiquetas, colores y
organización de la información, considerando el propósito de cada
dashboard y su audiencia.

La solución utiliza representaciones acordes con sus preguntas
analíticas: barras para comparar categorías, dispersión para explorar
relaciones, treemap para mostrar composición y mapas para explorar
diferencias geográficas. Streamlit organiza el análisis en pestañas
y permite segmentar los resultados mediante filtros.

Entre las fortalezas identificadas se encuentran la paleta compartida
entre notebooks y Streamlit, las escalas logarítmicas identificadas
en la dispersión financiera y la línea de referencia que compara
ingresos con presupuesto.

La revisión se concentra en comprobar la legibilidad de títulos y
etiquetas, la consistencia de colores y unidades, y la claridad de
las notas sobre cobertura y criterios de inclusión. También se
considera si las categorías numerosas o las exclusiones del mapa
requieren contexto adicional.

Las capturas revisadas muestran títulos, leyendas y notas de contexto
en los componentes comprobados. En el treemap, las categorías pequeñas
presentan etiquetas de menor legibilidad; su lectura puede apoyarse en
el detalle interactivo. No se realizó una prueba formal de accesibilidad
ni una evaluación con usuarios. Los cambios aplicados se registran en 9.7.

### 9.2.4 Analizar la interpretación

La revisión considera el mensaje principal de las visualizaciones
y las conclusiones que podría obtener un usuario no experto.

Los gráficos permiten describir el catálogo y explorar diferencias
entre contenidos, pero su interpretación debe respetar estos límites:

- Una mayor presencia de títulos por género o país no demuestra
  mayor preferencia o demanda de los usuarios.
- Una mayor popularidad TMDB no equivale a más reproducciones
  ni mayor engagement en StreamView.
- La correlación entre variables describe una asociación,
  pero no demuestra causalidad.
- Los indicadores financieros corresponden únicamente a las
  películas con datos disponibles. La razón ingresos/presupuesto
  no representa beneficio neto ni rentabilidad de la plataforma.
- Los conteos por año describen los títulos de la extracción,
  no necesariamente la evolución histórica del catálogo.

Por tanto, las recomendaciones deben vincularse con la evidencia
mostrada y presentarse como apoyo a la decisión, sin atribuir
a los datos conclusiones que no permiten demostrar.

### 9.2.5 Proponer mejoras

A partir de la evaluación, se proponen ajustes orientados a reforzar
el contexto y la claridad de la solución, conservando las
funcionalidades previamente aprobadas.

| Oportunidad | Mejora propuesta |
|---|---|
| Posible confusión entre popularidad y consumo. | Explicitar que la popularidad es un índice TMDB y revisar que la narrativa mantenga esta distinción. |
| Diferencias en la población utilizada para calcular indicadores. | Aclarar los criterios de inclusión y comprobar su consistencia entre visualizaciones. |
| Interpretación de resultados financieros. | Distinguir la razón agregada ingresos/presupuesto de las medidas por película y mantener visible la cobertura del análisis. |
| Países no representados en el mapa. | Informar las exclusiones por umbral de títulos o falta de correspondencia geográfica. |
| Posible sobreinterpretación de asociaciones o conteos temporales. | Reforzar las notas sobre causalidad y alcance de la extracción. |

Las propuestas se priorizaron según su aporte a la interpretación
y su viabilidad (9.6). Los cambios realizados y el alcance de sus
comprobaciones se registran en 9.7.

## 9.3 Revisión de errores frecuentes
Se revisan los seis errores del material 3.3.1. La tabla distingue
el diagnóstico inicial de la respuesta de esta etapa; no describe
todos los hallazgos como problemas que siguen presentes.

| Error | ¿Aplica? | Evidencia y valoración |
|---|---|---|
| KPI irrelevante | No identificado en la revisión inicial. | Los indicadores de catálogo, popularidad, valoración y finanzas responden a los objetivos de las audiencias definidas. |
| Mala pregunta analítica | Riesgo de desalineación detectado en la narrativa inicial. | La comparación de popularidad era pertinente, pero se utilizaba para responder sobre “enganche”. La narrativa se reformuló para mantener la pregunta dentro del alcance de TMDB; la inferencia excesiva se analiza también en 9.4. |
| Exceso de información | Riesgo localizado, no un problema general demostrado. | Las pestañas separan temas. En la captura de Géneros, las categorías pequeñas del treemap presentan etiquetas reducidas. Se mantiene como oportunidad de legibilidad; no se realizó una prueba de comprensión con usuarios. |
| Contexto insuficiente | Detectado parcialmente y atendido. | La cobertura financiera ya existía. Se reforzaron la definición de popularidad, las medidas financieras y las exclusiones del mapa; su presentación se comprobó en las capturas. |
| Mala escala | No identificada en la dispersión financiera revisada. | Se utilizan ejes logarítmicos etiquetados y una línea de referencia de ingresos iguales al presupuesto. La conclusión no se extiende a todos los gráficos sin revisarlos. |
| Comparaciones injustas | Inconsistencia inicial corregida en código. | Los promedios de directores y actores ahora excluyen registros sin votos, conservando el conteo total. Se realizaron pruebas sintéticas y revisión del detalle en interfaz; falta contraste independiente con los CSV. |

La revisión no considera cada oportunidad como un incumplimiento
de las entregas anteriores, sino como un aspecto que puede
optimizarse para fortalecer la interpretación de la solución.

## 9.4 Revisión de sesgos
Se revisan los cuatro sesgos del material 3.3.1, considerando
si la presentación puede inducir conclusiones distintas de
las que permiten sostener los datos. La valoración incluye el
diagnóstico inicial y las acciones posteriores.

| Sesgo | ¿Aplica? | Evidencia y valoración |
|---|---|---|
| Cherry picking | No identificado en la revisión inicial. | Los rankings se presentan como selecciones Top 10 y explicitan criterios como el mínimo de votos. Su existencia no demuestra una selección sesgada; debe mantenerse visible su alcance al utilizarlos en la narrativa. |
| Escalas truncadas | No identificado en los elementos revisados. | El ranking de calificaciones fija el eje entre 0 y 10. La dispersión financiera identifica sus escalas logarítmicas, que no constituyen por sí mismas una truncación engañosa. |
| Color engañoso | Riesgo potencial, no confirmado. | Existe una paleta compartida para películas y series. Se debe comprobar que los colores utilizados para categorías y resultados financieros no produzcan confusión dentro de las visualizaciones. |
| Sobreinterpretación | Identificada y atendida en la narrativa. | Se retiraron afirmaciones de mayor “enganche” y recomendaciones automáticas no sustentadas. Se explicitaron límites de causalidad y cobertura financiera. El responsable reportó la ejecución del notebook actualizado sin errores. |

La evaluación distingue entre sesgos identificados y riesgos
potenciales. Las medidas adoptadas y su validación se registran
en el apartado 9.7.

## 9.5 Fortalezas de la solución

La evaluación identifica las siguientes fortalezas en la solución
desarrollada:

- Orientación a distintas audiencias: Power BI ofrece una visión
  ejecutiva, mientras Streamlit permite una exploración más detallada
  para la Gerencia de Contenidos y Adquisición.
- Organización e interactividad: las pestañas y filtros de Streamlit
  permiten explorar los temas sin presentar toda la información
  simultáneamente.
- Contexto financiero: se informa dinámicamente la cantidad y
  proporción de películas incluidas en el análisis financiero.
- Criterios de valoración: el indicador general de calificación
  excluye títulos sin votos y el ranking de mejor evaluados exige
  un mínimo de evaluaciones.
- Representación financiera: la dispersión utiliza escalas
  logarítmicas identificadas y una línea de referencia de ingresos
  iguales al presupuesto.
- Consistencia y mantenimiento: las funciones y la paleta compartidas
  entre notebooks y Streamlit facilitan la coherencia del proyecto.

Estas características constituyen una base para la optimización.
Su reconocimiento no implica que todos los componentes hayan sido
validados nuevamente en ejecución durante esta evaluación.

## 9.6 Limitaciones y oportunidades de mejora
La solución presenta limitaciones asociadas a la disponibilidad de
datos y oportunidades para reforzar su comunicación. Se distinguen
los límites de los datos de los ajustes priorizados a partir del
diagnóstico inicial. El estado posterior de cada cambio se indica en 9.7.

| Limitación u oportunidad | Acción propuesta | Impacto |
|---|---|---|
| La popularidad TMDB no representa consumo ni engagement. | Incorporar una advertencia visible y ajustar las afirmaciones de la narrativa que excedan el alcance del indicador. | Alto |
| El tratamiento de títulos sin votos difiere entre el KPI general y las calificaciones de directores y actores. | Unificar el criterio de cálculo y explicar la población utilizada. | Alto |
| La información financiera cubre aproximadamente el 22 % de las películas. | Mantener visible la cobertura y evitar generalizar los resultados al catálogo completo. | Alto |
| Las medidas financieras agregadas y por película pueden confundirse. | Diferenciar la razón de totales, el promedio individual y la mediana mediante etiquetas y explicaciones claras. | Alto |
| El mapa puede excluir países por umbral o falta de código. En la selección general comprobada no hubo exclusiones por código entre los países elegibles. | Explicar ambos motivos y permitir consultar los países excluidos cuando corresponda. | Medio |
| Las correlaciones y los conteos temporales pueden sobreinterpretarse. | Reforzar las notas sobre asociación, causalidad y alcance temporal de la extracción. | Medio |
| Las etiquetas de categorías pequeñas del treemap tienen legibilidad limitada en la vista general. | Evaluar una vista complementaria o simplificación si una prueba de lectura lo justifica, conservando acceso al detalle. | Medio |
| Algunos títulos pueden afinarse sin modificar la pregunta analítica. | Revisar su redacción en el cierre editorial, sin presentar como hallazgo una conclusión no comprobada. | Bajo |

La prioridad considera el riesgo de una interpretación incorrecta
y su efecto sobre las decisiones. Una acción de alto impacto puede
consistir en aclarar información existente, sin añadir funcionalidades.

Las propuestas no se consideran implementadas hasta registrar
el cambio y comprobar su funcionamiento. Las limitaciones de
cobertura permanecen aunque se mejore su comunicación.


## 9.7 Mejoras implementadas y validación

Se implementaron ajustes de contexto y consistencia sobre el
dashboard existente, conservando sus filtros, pestañas, fuentes,
paleta y reglas financieras.

La validación comprendió revisión de sintaxis, pruebas con datos
sintéticos de la función de agregación y comprobaciones visuales
de la aplicación ejecutada localmente. Se recopilaron capturas
de los escenarios revisados para documentar los indicadores,
las notas explicativas y las respuestas de la aplicación ante
selecciones particulares.

Se distingue entre la comprobación visual y funcional del
dashboard y el contraste independiente de sus resultados con
los CSV procesados. Las capturas permiten verificar lo mostrado
por la aplicación, pero no sustituyen un recálculo independiente.

| Mejora | Cambio realizado | Validación | Estado |
|---|---|---|---|
| Contexto de popularidad y narrativa | Se incorporó una nota que distingue el índice TMDB de reproducciones, engagement y retención. Se revisó el notebook para retirar inferencias y recomendaciones que excedían la evidencia. | Las capturas muestran la advertencia de alcance en la aplicación. La revisión editorial y la ejecución sin errores del notebook corresponden a la comprobación local previamente registrada por el responsable. | Implementada; nota comprobada visualmente. Revisión editorial y ejecución local del notebook registradas por el responsable. |
| Calificaciones de directores y actores | Se conserva el conteo total de títulos y se calcula la calificación únicamente con títulos con votos. Se informa por separado la cantidad de títulos evaluados. | Las pruebas sintéticas previamente realizadas verificaron el criterio de agregación. En el ranking de directores, el tooltip de Dominic Zapata muestra 21 títulos, 5 evaluados y calificación con votos de 8,4. En el ranking de actores, Min Do-yoon presenta 111 títulos, 80 evaluados y calificación con votos de aproximadamente 5,18. Las capturas corroboran la presentación diferenciada de estos valores. | Implementada; comprobación visual de ambos rankings y pruebas sintéticas registradas. El contraste independiente con los CSV no se realizó en esta revisión. |
| Contexto de correlación | Se añadió el tamaño de muestra, la advertencia de no causalidad y el manejo de datos insuficientes o sin variación. | En la selección general se muestra Spearman de 0,32 sobre 27.431 títulos con votos y datos en ambas variables, junto con la explicación de que describe una asociación monótona y no una relación causal. Al fijar el rango de calificación en 8,00–8,00, se muestran 853 títulos filtrados y 851 con votos; la aplicación informa que la correlación no está disponible porque se requieren datos y variación en ambas variables, sin presentar un coeficiente numérico. | Implementada y comprobada visualmente en el escenario general y en el caso sin variación en la calificación. El caso específico de menos de dos observaciones no se comprobó por separado. |
| Claridad financiera | Se diferenciaron el ROI agregado, la mediana y el promedio por película mediante etiquetas y tarjetas. Se aclaró el alcance de estas medidas y de la cobertura financiera. | Con los filtros generales se muestran ROI agregado de 2,92x, mediana de 1,70x y promedio de 4,29x, junto con una cobertura de 3.523 de 16.000 películas (22,0 %). La nota explica que el ROI agregado divide las sumas de ingresos y presupuesto, mientras que el promedio y la mediana resumen las razones individuales. También aclara que estos múltiplos no representan beneficio neto ni rentabilidad de StreamView y que la cobertura parcial no garantiza representatividad del catálogo. | Implementada y comprobada visualmente en sus etiquetas, valores y explicaciones. El contraste independiente de los cálculos con los CSV no se realizó en esta revisión. |
| Transparencia del mapa | Se añadieron notas y tablas que distinguen exclusiones por mínimo de títulos y por falta de código ISO-3. Se explicitó que ambas métricas utilizan títulos con votos. | Se comprobó la presentación de calificación promedio y popularidad promedio. En la selección general se muestran 86 países representados, 60 por debajo del mínimo de 5 títulos con votos y 0 países que cumplen el mínimo pero carecen de código ISO-3. La tabla desplegada permite consultar países excluidos por cantidad insuficiente de títulos con votos. | Implementada y comprobada visualmente para ambas métricas y para las exclusiones por umbral. El escenario con países elegibles sin código ISO-3 no se observó y no se considera probado. |
| Contexto de géneros | Se explicó la población utilizada en los promedios y la pertenencia de un título a varios géneros. | Se comprobó que la pestaña informa que ambos promedios utilizan géneros con al menos 30 títulos con votos, mientras que el KPI general de popularidad incluye todos los títulos filtrados. Bajo el treemap se aclara que un título puede pertenecer a varios géneros y que la suma de categorías no equivale necesariamente al total de títulos únicos. | Implementada; ambas notas y sus visualizaciones fueron comprobadas visualmente. |

### Pruebas de regresión

Se revisaron dos comportamientos preexistentes para comprobar
que se conservaran tras los ajustes:

- Solo series: en la prueba realizada por el responsable con
  únicamente TV Show seleccionado, la pestaña Finanzas mostró
  el aviso de que los datos financieros existen solo para
  películas y solicitó incluir Movie para consultar el análisis.
  No se mostraron tarjetas ni gráficos financieros con valores
  sustituidos por cero. La captura documenta el aviso y la
  ausencia del bloque financiero; el selector de tipo de
  contenido quedó fuera del recorte.

- Sin tipos de contenido seleccionados: se comprobó, con el
  selector vacío visible en la captura, que la aplicación
  muestra el aviso «Ningún título cumple los filtros
  seleccionados. Amplía los rangos», sin presentar indicadores
  ni gráficos.

### Alcance y limitaciones de la validación

No se observaron errores visibles en las capturas de los
escenarios documentados. Se corroboraron la presentación de
los cambios, las notas de contexto, los detalles de los
rankings, la alternancia de métricas del mapa y el manejo
del caso de correlación sin variación.

Estas comprobaciones no constituyen una validación exhaustiva
ni una auditoría independiente de los cálculos. El contraste
de las calificaciones de directores y actores y de los
indicadores financieros con los CSV procesados permanece
pendiente. Tampoco se comprobó por separado el escenario de
correlación con menos de dos observaciones.

Con los datos y filtros revisados no se presentó ningún país
que cumpliera el mínimo de títulos con votos y careciera de
código ISO-3. Por tanto, ese escenario se registra como no
observado, sin atribuirle una prueba que no se realizó.
