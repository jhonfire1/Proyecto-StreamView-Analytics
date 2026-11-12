# 9. Evaluación crítica de la solución

## 9.1 Objetivo y alcance

La evaluación crítica tiene como propósito analizar la efectividad de la
solución de visualización desarrollada en las experiencias anteriores e
identificar oportunidades para fortalecer su claridad, interpretación y
utilidad para la toma de decisiones.

Se toma como punto de partida la solución previamente aprobada. La
revisión no busca reconstruir las funcionalidades existentes, sino
reconocer sus fortalezas, explicitar sus limitaciones y justificar
oportunidades de optimización.

La evaluación considera el dashboard ejecutivo de Power BI, el dashboard
analítico de Streamlit y las visualizaciones de la narrativa (Data
Storytelling). Se revisaron y comprobaron los componentes de ambas
herramientas, incluyendo la actualización directa del archivo
`DashBoard_Ejecutivo.pbix` en Power BI mediante ocho intervenciones
identificadas como BI01--BI08. Asimismo, se verificaron las mejoras
funcionales y de contexto implementadas en Streamlit y los ajustes
realizados en el notebook de storytelling.

La evaluación integra las evidencias de las tres partes de la solución,
considerando los cambios efectivamente realizados y el alcance de las
comprobaciones documentadas.

Se aplica el marco de cinco pasos del material «3.3.1 Evaluación Crítica
de las Visualizaciones»: comprender el objetivo, revisar los datos,
evaluar la representación, analizar la interpretación y proponer
mejoras.

Se distingue entre:

-   Funcionalidades y fortalezas existentes.
-   Limitaciones de los datos.
-   Oportunidades de mejora.
-   Cambios efectivamente implementados y comprobados.

## 9.2 Aplicación del marco de evaluación

### 9.2.1 Comprender el objetivo

La solución de StreamView Analytics tiene como objetivo transformar la
información del catálogo audiovisual en visualizaciones que faciliten su
exploración y apoyen decisiones relacionadas con la composición del
catálogo, la evaluación de contenidos y la identificación de
oportunidades de adquisición.

Para evaluar su pertinencia, se distinguen dos audiencias principales:

  -----------------------------------------------------------------------
  Dashboard         Audiencia         Propósito         Decisiones que
                                                        busca apoyar
  ----------------- ----------------- ----------------- -----------------
  Ejecutivo en      Directorio y      Entregar una      Monitorear el
  Power BI          Gerencia General  visión panorámica portafolio y
                                      del estado y      orientar la
                                      composición del   priorización
                                      catálogo.         estratégica según
                                                        formato, género,
                                                        país y periodo.

  Analítico en      Gerencia de       Explorar          Identificar
  Streamlit         Contenidos y      detalladamente    títulos, géneros
                    Adquisición       popularidad,      y mercados que
                                      calificaciones,   conviene evaluar
                                      géneros, países,  para adquisición
                                      rankings y        o renovación.
                                      resultados        
                                      financieros.      
  -----------------------------------------------------------------------

La evaluación considera si los indicadores y visualizaciones contribuyen
a estos propósitos y si su interpretación se mantiene dentro del alcance
de las fuentes disponibles.

La popularidad y la valoración permiten comparar características de los
contenidos, pero no deben interpretarse como medidas directas de
reproducciones, retención o comportamiento de los suscriptores.

Asimismo, el análisis financiero se limita a películas que cumplen los
criterios de disponibilidad de presupuesto e ingresos definidos en el
proyecto. No corresponde extender sus resultados financieros a las
series ni a contenidos sin dicha información.

### 9.2.2 Revisar los datos

El proyecto utiliza los conjuntos de películas y series proporcionados
para StreamView Analytics. Según la documentación de preparación, los
datos procesados contienen 16.000 películas y 15.991 series, con años de
estreno entre 2010 y 2025.

Las fuentes permiten analizar la composición del catálogo, popularidad,
valoración y resultados financieros disponibles. Su interpretación
considera las siguientes limitaciones:

-   **Popularidad:** es un índice relativo de TMDB, no una medida de
    reproducciones, engagement o retención.
-   **Calificación:** debe analizarse junto con la cantidad de votos.
    Los títulos sin votos no equivalen a contenidos mal evaluados.
-   **Evaluaciones disponibles:** en la selección general se muestran
    27.431 títulos con votos de un total de 31.991; la diferencia es de
    4.560 títulos sin votos.
-   **Finanzas:** el análisis incluye únicamente películas que cumplen
    la regla de presupuesto e ingresos del proyecto, con una cobertura
    aproximada del 22 % de las películas. Sus resultados no deben
    generalizarse a todo el catálogo ni a las series.
-   **Países y géneros:** un título puede pertenecer a varias
    categorías, por lo que sus conteos no siempre suman el total de
    títulos únicos.
-   **Temporalidad:** la distribución aproximadamente uniforme reportada
    por año no permite concluir que exista crecimiento o estabilidad
    real del catálogo.
-   **Muestreo estratificado:** el conjunto contiene exactamente 1.000
    películas y 1.000 series por año de estreno entre 2010 y 2025, con
    991 series en 2025 después de eliminar registros duplicados. Por
    esta razón, los conteos anuales responden al diseño de extracción de
    los datos y no representan necesariamente el crecimiento histórico
    real del catálogo.

En conclusión, los datos son pertinentes para los objetivos descriptivos
del proyecto, siempre que se expliciten su cobertura, las reglas de
inclusión y los límites de las conclusiones.

### 9.2.3 Evaluar la representación

Se revisan los tipos de gráficos, escalas, etiquetas, colores y
organización de la información, considerando el propósito de cada
dashboard y su audiencia.

La solución utiliza representaciones acordes con sus preguntas
analíticas: barras para comparar categorías, dispersión para explorar
relaciones, treemap para mostrar composición y mapas para explorar
diferencias geográficas. Streamlit organiza el análisis en pestañas y
permite segmentar los resultados mediante filtros.

Entre las fortalezas identificadas se encuentran la consistencia
cromática de las visualizaciones, con películas representadas en rojo
(`#E50914`), series en azul (`#1F77B4`) y totales por país en verde
neutro, aplicada en Power BI y Streamlit. También destacan las escalas
logarítmicas identificadas en las visualizaciones financieras y de
popularidad, junto con la línea de referencia que compara ingresos con
presupuesto de producción.

En Power BI se reforzó la identificación de los indicadores mediante
subtítulos y notas explicativas, mientras que Streamlit incorpora
información contextual y detalles interactivos para facilitar la
interpretación de los resultados.

La revisión se concentra en comprobar la legibilidad de títulos y
etiquetas, la consistencia de colores y unidades, y la claridad de las
notas sobre cobertura y criterios de inclusión. También se considera si
las categorías numerosas o las exclusiones del mapa requieren contexto
adicional.

Las comprobaciones documentadas muestran títulos, subtítulos, leyendas y
notas de contexto en los componentes revisados de ambas herramientas. En
el treemap, las categorías pequeñas presentan etiquetas de menor
legibilidad en la vista general, aunque su lectura puede apoyarse en los
tooltips interactivos. No se realizó una prueba formal de accesibilidad
ni una evaluación con usuarios.

### 9.2.4 Analizar la interpretación

La revisión considera el mensaje principal de las visualizaciones y las
conclusiones que podría obtener un usuario no experto.

Los gráficos permiten describir el catálogo y explorar diferencias entre
contenidos, pero su interpretación debe respetar estos límites:

-   Una mayor presencia de títulos por género o país no demuestra mayor
    preferencia o demanda de los usuarios.
-   Una mayor popularidad TMDB no equivale a más reproducciones ni mayor
    engagement en StreamView.
-   La correlación entre variables describe una asociación, pero no
    demuestra causalidad.
-   Los indicadores financieros corresponden únicamente a las películas
    con datos disponibles. La razón ingresos/presupuesto no representa
    beneficio neto ni rentabilidad de la plataforma.
-   Los conteos por año describen los títulos de la extracción, no
    necesariamente la evolución histórica del catálogo.

Por tanto, las recomendaciones deben vincularse con la evidencia
mostrada y presentarse como apoyo a la decisión, sin atribuir a los
datos conclusiones que no permiten demostrar.

### 9.2.5 Proponer mejoras

A partir de la evaluación, se identificaron oportunidades de mejora
orientadas a reforzar el contexto, la consistencia metodológica y la
claridad de la solución. Durante esta etapa se implementaron ajustes en
ambas herramientas y en la narrativa visual. Se distinguen las acciones
ya ejecutadas de las oportunidades que permanecen pendientes.

  -----------------------------------------------------------------------
  Oportunidad identificada            Acción realizada o pendiente
  ----------------------------------- -----------------------------------
  Posible confusión entre popularidad Se incorporó una advertencia sobre
  y consumo.                          el índice TMDB y se ajustó la
                                      narrativa para evitar inferencias
                                      sobre reproducciones o engagement.

  Diferencias en la población         Se corrigieron los promedios de
  utilizada para calcular             calificación para excluir títulos
  indicadores.                        sin votos y se explicitó la
                                      población evaluada.

  Interpretación de resultados        Se diferenciaron ROI agregado,
  financieros.                        mediana y promedio individual,
                                      manteniendo visible la cobertura
                                      del 22 %.

  Países no representados en el mapa. Se documentaron las exclusiones por
                                      umbral mínimo y por ausencia de
                                      código geográfico cuando
                                      corresponda.

  Posible sobreinterpretación de      Se incorporaron advertencias sobre
  asociaciones y conteos temporales.  causalidad y muestreo
                                      estratificado.

  Legibilidad de categorías pequeñas  Se mantiene como oportunidad de
  en el treemap.                      mejora futura, considerando una
                                      vista complementaria si una
                                      evaluación posterior lo justifica.
  -----------------------------------------------------------------------

Las propuestas y acciones se priorizaron según su aporte a la
interpretación y su viabilidad. Una acción de alto impacto puede
consistir en aclarar información existente, sin añadir funcionalidades.

Las propuestas no se consideran implementadas hasta registrar el cambio
y comprobar su funcionamiento. Las limitaciones de cobertura permanecen
aunque se mejore su comunicación.

## 9.3 Revisión de errores frecuentes

Se revisan los seis errores del material 3.3.1. La tabla presenta el
diagnóstico y las acciones realizadas durante esta etapa.

  -----------------------------------------------------------------------
  Error                   ¿Aplica?                Evidencia y valoración
  ----------------------- ----------------------- -----------------------
  KPI irrelevante         No aplica.              Los indicadores
                                                  responden a preguntas
                                                  estratégicas
                                                  relacionadas con
                                                  composición, calidad y
                                                  desempeño financiero
                                                  del catálogo.

  Mala pregunta analítica Corregido.              Se reformuló la
                                                  narrativa para evitar
                                                  interpretar la
                                                  popularidad TMDB como
                                                  una medida de
                                                  engagement de los
                                                  usuarios.

  Exceso de información   Mitigado.               La separación en cinco
                                                  pestañas de Streamlit y
                                                  la vista ejecutiva de
                                                  Power BI permiten
                                                  distribuir la
                                                  información según las
                                                  necesidades de cada
                                                  audiencia.

  Contexto insuficiente   Corregido.              Se incorporaron notas
                                                  sobre cobertura
                                                  financiera, títulos con
                                                  votos, muestreo
                                                  estratificado y
                                                  exclusiones
                                                  geográficas.

  Mala escala             Mitigado.               Se identifican las
                                                  escalas logarítmicas en
                                                  las visualizaciones
                                                  correspondientes y se
                                                  incorpora la línea de
                                                  equilibrio ROI = 1 en
                                                  la representación
                                                  financiera.

  Comparaciones injustas  Corregido.              Se excluyeron los
                                                  títulos sin votos del
                                                  cálculo de
                                                  calificaciones en los
                                                  rankings de directores
                                                  y actores de Streamlit
                                                  y en el KPI general de
                                                  Power BI.
  -----------------------------------------------------------------------

## 9.4 Revisión de sesgos

Se revisan los cuatro sesgos del material 3.3.1, considerando si la
presentación puede inducir conclusiones distintas de las que permiten
sostener los datos. La valoración incluye el diagnóstico inicial y las
acciones posteriores.

  -----------------------------------------------------------------------
  Sesgo                   ¿Aplica?                Evidencia y valoración
  ----------------------- ----------------------- -----------------------
  Cherry picking          No identificado en la   Los rankings se
                          revisión.               presentan como
                                                  selecciones Top 10 y
                                                  explicitan criterios
                                                  como el mínimo de 50
                                                  votos. Su existencia no
                                                  demuestra una selección
                                                  sesgada; debe
                                                  mantenerse visible su
                                                  alcance al utilizarlos
                                                  en la narrativa.

  Escalas truncadas       No identificado en los  El ranking de
                          elementos revisados.    calificaciones mantiene
                                                  la escala completa de 0
                                                  a 10. Las escalas
                                                  logarítmicas están
                                                  identificadas en las
                                                  visualizaciones
                                                  correspondientes y no
                                                  constituyen por sí
                                                  mismas una truncación
                                                  engañosa.

  Color engañoso          Corregido.              Se unificó la paleta
                                                  cromática en Power BI y
                                                  Streamlit: rojo
                                                  (`#E50914`) para
                                                  películas, azul
                                                  (`#1F77B4`) para series
                                                  y verde neutro para
                                                  totales. Esta
                                                  estandarización
                                                  facilita la
                                                  identificación
                                                  consistente de las
                                                  categorías.

  Sobreinterpretación     Corregido.              Se retiraron
                                                  afirmaciones causales y
                                                  referencias a mayor
                                                  «enganche» que no
                                                  estaban sustentadas.
                                                  También se
                                                  diferenciaron
                                                  explícitamente las
                                                  medidas financieras y
                                                  se acotó su alcance
                                                  histórico.
  -----------------------------------------------------------------------

La evaluación distingue entre sesgos identificados y riesgos
potenciales. Las medidas adoptadas y su validación se registran en el
apartado 9.7.

## 9.5 Fortalezas de la solución

La evaluación identifica las siguientes fortalezas en la solución
desarrollada:

-   **Orientación a distintas audiencias:** Power BI ofrece una visión
    ejecutiva, mientras Streamlit permite una exploración más detallada
    para la Gerencia de Contenidos y Adquisición.
-   **Organización e interactividad:** las pestañas y filtros de
    Streamlit permiten explorar los temas sin presentar toda la
    información simultáneamente.
-   **Contexto financiero:** se informa dinámicamente la cantidad y
    proporción de películas incluidas en el análisis financiero.
-   **Criterios de valoración:** el indicador general de calificación
    excluye títulos sin votos y el ranking de mejor evaluados exige un
    mínimo de evaluaciones.
-   **Representación financiera:** la dispersión utiliza escalas
    logarítmicas identificadas y una línea de referencia de ingresos
    iguales al presupuesto.
-   **Consistencia y mantenimiento:** las funciones y la paleta
    compartidas entre notebooks y Streamlit facilitan la coherencia del
    proyecto.
-   **Consistencia entre herramientas:** Power BI y Streamlit utilizan
    una paleta cromática unificada, diferenciando películas, series y
    totales mediante colores consistentes.
-   **Corrección metodológica de indicadores:** ambas herramientas
    excluyen los títulos sin votos de los promedios de calificación,
    evitando que los registros sin evaluaciones reduzcan artificialmente
    los resultados.

Estas características constituyen una base para la optimización. Su
reconocimiento no implica que todos los componentes hayan sido sometidos
a una auditoría independiente de sus cálculos.

## 9.6 Limitaciones y oportunidades de mejora

La solución presenta limitaciones asociadas a la disponibilidad de datos
y oportunidades para reforzar su comunicación. Se distinguen los límites
de los datos de los ajustes priorizados a partir del diagnóstico
inicial. El estado posterior de cada cambio se indica en 9.7.

  -----------------------------------------------------------------------
  Limitación u            Acción realizada o      Impacto
  oportunidad             pendiente               
  ----------------------- ----------------------- -----------------------
  La popularidad TMDB no  Se incorporó una        Alto
  representa consumo ni   advertencia en las      
  engagement.             herramientas y se       
                          ajustó la narrativa     
                          para evitar inferencias 
                          sobre consumo interno.  

  Los títulos sin votos   Se corrigió el criterio Alto
  afectan la              de cálculo en Streamlit 
  interpretación de las   y Power BI, excluyendo  
  calificaciones.         los títulos sin votos   
                          de los promedios.       

  La información          Se explicitó la         Alto
  financiera cubre        cobertura y los         
  aproximadamente el 22 % criterios de inclusión. 
  de las películas.       La limitación de los    
                          datos permanece.        

  Las medidas financieras Se diferenciaron el ROI Alto
  agregadas y por         agregado, la mediana y  
  película pueden         el promedio individual  
  confundirse.            mediante etiquetas y    
                          explicaciones.          

  El mapa puede excluir   Se incorporaron notas y Medio
  países por umbral o     tablas explicativas en  
  falta de código.        Streamlit y una         
                          aclaración sobre        
                          registros «Sin dato» en 
                          Power BI.               

  Las correlaciones y los Se incorporaron         Medio
  conteos temporales      advertencias sobre      
  pueden                  causalidad y muestreo   
  sobreinterpretarse.     estratificado.          

  Las etiquetas de        Se mantiene como        Medio
  categorías pequeñas del oportunidad de mejora   
  treemap tienen          futura; puede evaluarse 
  legibilidad limitada en una vista               
  la vista general.       complementaria si una   
                          prueba posterior lo     
                          justifica.              
  -----------------------------------------------------------------------

La prioridad considera el riesgo de una interpretación incorrecta y su
efecto sobre las decisiones. Una acción de alto impacto puede consistir
en aclarar información existente, sin añadir funcionalidades.

Las mejoras de comunicación no eliminan las limitaciones estructurales
de los datos. En particular, la cobertura financiera parcial, la
ausencia de votos en determinados títulos y el diseño estratificado de
la extracción continúan condicionando el alcance de las conclusiones.

## 9.7 Mejoras implementadas y validación

Se implementaron ajustes de contexto y consistencia sobre los dashboards
existentes, conservando sus filtros, pestañas, fuentes, paleta y reglas
financieras.

La validación comprendió revisión de sintaxis, pruebas con datos
sintéticos de la función de agregación y comprobaciones funcionales y
visuales de la aplicación ejecutada localmente con los CSV procesados
del proyecto. También se realizó la revisión, modificación y validación
directa del archivo `DashBoard_Ejecutivo.pbix` en Power BI Desktop,
documentada mediante las intervenciones BI01--BI08.

Se recopilaron capturas de los escenarios revisados para documentar los
indicadores, las notas explicativas y las respuestas de las aplicaciones
ante distintas selecciones. Las comprobaciones permiten verificar el
funcionamiento observado con los datos reales del proyecto, sin
constituir una auditoría independiente de todos los cálculos.

### 9.7.1 Mejoras implementadas en Streamlit y Storytelling

  -------------------------------------------------------------------------
  Mejora            Cambio realizado  Validación          Estado
  ----------------- ----------------- ------------------- -----------------
  Contexto de       Se incorporó una  Las capturas        Implementada;
  popularidad y     nota que          muestran la         nota comprobada
  narrativa         distingue el      advertencia de      visualmente.
                    índice TMDB de    alcance en la       Revisión
                    reproducciones,   aplicación. La      editorial y
                    engagement y      revisión editorial  ejecución local
                    retención. Se     y la ejecución sin  del notebook
                    revisó el         errores del         completadas según
                    notebook para     notebook            el registro del
                    retirar           corresponden a la   responsable.
                    inferencias y     comprobación local  
                    recomendaciones   previamente         
                    que excedían la   registrada por el   
                    evidencia.        responsable.        

  Calificaciones de Se conserva el    Las pruebas         Implementada;
  directores y      conteo total de   sintéticas          criterio de
  actores           títulos y se      previamente         agregación
                    calcula la        realizadas          comprobado
                    calificación      verificaron el      mediante pruebas
                    únicamente con    criterio de         sintéticas y
                    títulos con       agregación. Con los presentación de
                    votos. Se informa CSV procesados      ambos rankings
                    por separado la   cargados en el      verificada con
                    cantidad de       dashboard, el       los datos reales
                    títulos           tooltip de Dominic  del proyecto.
                    evaluados.        Zapata muestra 21   
                                      títulos, 5          
                                      evaluados y         
                                      calificación con    
                                      votos de 8,4. En el 
                                      ranking de actores, 
                                      Min Do-yoon         
                                      presenta 111        
                                      títulos, 80         
                                      evaluados y         
                                      calificación con    
                                      votos de            
                                      aproximadamente     
                                      5,18. Las capturas  
                                      corroboran la       
                                      presentación        
                                      diferenciada de     
                                      estos valores.      

  Contexto de       Se añadió el      En la selección     Implementada y
  correlación       tamaño de         general se muestra  comprobada
                    muestra, la       Spearman de 0,32    funcional y
                    advertencia de no sobre 27.431        visualmente en el
                    causalidad y el   títulos con votos y escenario general
                    manejo de datos   datos en ambas      y en el caso sin
                    insuficientes o   variables, junto    variación en la
                    sin variación.    con la explicación  calificación.
                                      de que describe una 
                                      asociación monótona 
                                      y no una relación   
                                      causal. Al fijar el 
                                      rango de            
                                      calificación en     
                                      8,00--8,00, se      
                                      muestran 853        
                                      títulos filtrados y 
                                      851 con votos; la   
                                      aplicación informa  
                                      que la correlación  
                                      no está disponible  
                                      porque se requieren 
                                      datos y variación   
                                      en ambas variables, 
                                      sin presentar un    
                                      coeficiente         
                                      numérico.           

  Claridad          Se diferenciaron  Con los CSV         Implementada;
  financiera        el ROI agregado,  procesados y los    indicadores,
                    la mediana y el   filtros generales   cobertura,
                    promedio por      se muestran ROI     etiquetas y
                    película mediante agregado de 2,92x,  explicaciones
                    etiquetas y       mediana de 1,70x y  comprobados
                    tarjetas. Se      promedio de 4,29x,  funcional y
                    aclaró el alcance junto con una       visualmente con
                    de estas medidas  cobertura de 3.523  los datos reales
                    y de la cobertura de 16.000 películas del proyecto.
                    financiera.       (22,0 %). La nota   
                                      explica que el ROI  
                                      agregado divide las 
                                      sumas de ingresos y 
                                      presupuesto,        
                                      mientras que el     
                                      promedio y la       
                                      mediana resumen las 
                                      razones             
                                      individuales.       
                                      También aclara que  
                                      estos múltiplos no  
                                      representan         
                                      beneficio neto ni   
                                      rentabilidad de     
                                      StreamView y que la 
                                      cobertura parcial   
                                      no garantiza        
                                      representatividad   
                                      del catálogo.       

  Transparencia del Se añadieron      Se comprobó la      Implementada y
  mapa              notas y tablas    presentación de     comprobada para
                    que distinguen    calificación        ambas métricas y
                    exclusiones por   promedio y          para las
                    mínimo de títulos popularidad         exclusiones por
                    y por falta de    promedio. En la     umbral. El
                    código ISO-3. Se  selección general   escenario con
                    explicitó que     se muestran 86      países elegibles
                    ambas métricas    países              sin código ISO-3
                    utilizan títulos  representados, 60   no se observó con
                    con votos.        por debajo del      los datos
                                      mínimo de 5 títulos revisados y no se
                                      con votos y 0       considera
                                      países que cumplen  probado.
                                      el mínimo pero      
                                      carecen de código   
                                      ISO-3. La tabla     
                                      desplegada permite  
                                      consultar países    
                                      excluidos por       
                                      cantidad            
                                      insuficiente de     
                                      títulos con votos.  

  Contexto de       Se explicó la     Se comprobó que la  Implementada;
  géneros           población         pestaña informa que ambas notas y sus
                    utilizada en los  ambos promedios     visualizaciones
                    promedios y la    utilizan géneros    fueron
                    pertenencia de un con al menos 30     comprobadas
                    título a varios   títulos con votos,  visualmente con
                    géneros.          mientras que el KPI los datos reales
                                      general de          del proyecto.
                                      popularidad incluye 
                                      todos los títulos   
                                      filtrados. Bajo el  
                                      treemap se aclara   
                                      que un título puede 
                                      pertenecer a varios 
                                      géneros y que la    
                                      suma de categorías  
                                      no equivale         
                                      necesariamente al   
                                      total de títulos    
                                      únicos.             
  -------------------------------------------------------------------------

### 9.7.2 Mejoras implementadas en Power BI

Además de las mejoras implementadas en Streamlit y en la narrativa
visual, se realizó una revisión directa del archivo
`DashBoard_Ejecutivo.pbix` en Power BI Desktop. Esta intervención
permitió corregir aspectos de presentación, consistencia metodológica,
interpretación de indicadores y configuración de las fuentes de datos.

Se documentaron ocho intervenciones, identificadas como BI01--BI08:

  ------------------------------------------------------------------------------------
  ID                Elemento          Cambio realizado               Validación
  ----------------- ----------------- ------------------------------ -----------------
  BI01              Paleta cromática  Se unificaron los colores en   Ajustado y
                                      todo el lienzo: películas en   comprobado.
                                      rojo (`#E50914`), series en    
                                      azul (`#1F77B4`) y barras de   
                                      totales por país en verde      
                                      neutro.                        

  BI02              Popularidad       Se incorporó en la tarjeta     Ajustado y
                                      Popularidad Promedio (42,63)   comprobado.
                                      la nota visible «Índice        
                                      relativo TMDB».                

  BI03              Calificación      Se filtró `vote_count > 0` en  Ajustado y
                                      Calificación Promedio y se     comprobado.
                                      añadió la nota «Títulos con    
                                      votos (27.431)», corrigiendo   
                                      el sesgo inicial de 5,69 a     
                                      6,63, consistente con          
                                      Streamlit.                     

  BI04              Visualización     Se renombró el gráfico a       Ajustado y
                    temporal          «Distribución por Año de       comprobado.
                                      Estreno» y se agregó el        
                                      subtítulo «Muestra             
                                      estratificada (máx. 1.000      
                                      títulos/año por tipo; no es el 
                                      crecimiento real)».            

  BI05              Países y géneros  Se añadieron subtítulos que    Ajustado y
                                      aclaran la pertenencia         comprobado.
                                      múltiple de títulos a varios   
                                      países o géneros.              

  BI06              Mapa              Se precisó en el subtítulo que Ajustado y
                                      el mapa excluye registros      comprobado.
                                      clasificados como «Sin dato».  

  BI07              Filtros y títulos Se comprobó la respuesta       Verificado sin
                                      dinámica de los segmentadores  cambios.
                                      de año (2010--2025), género y  
                                      tipo, junto con la coherencia  
                                      de los títulos.                

  BI08              Fuentes           Se reconfiguró el origen de    Ajustado y
                                      `netflix_movies_cleaned.csv` y comprobado.
                                      `netflix_tv_cleaned.csv` hacia 
                                      `data/processed/` y se         
                                      verificó su actualización sin  
                                      errores.                       
  ------------------------------------------------------------------------------------

Estas intervenciones permitieron alinear el dashboard ejecutivo con los
criterios metodológicos y visuales utilizados en Streamlit, manteniendo
la diferenciación de audiencias y el propósito comunicacional de cada
herramienta.

### 9.7.3 Pruebas de regresión

Se revisaron dos comportamientos preexistentes para comprobar que se
conservaran tras los ajustes:

-   **Solo series:** en la prueba realizada por el responsable con
    únicamente TV Show seleccionado, la pestaña Finanzas mostró el aviso
    de que los datos financieros existen solo para películas y solicitó
    incluir Movie para consultar el análisis. No se mostraron tarjetas
    ni gráficos financieros con valores sustituidos por cero. La captura
    documenta el aviso y la ausencia del bloque financiero; el selector
    de tipo de contenido quedó fuera del recorte.
-   **Sin tipos de contenido seleccionados:** se comprobó, con el
    selector vacío visible en la captura, que la aplicación muestra el
    aviso «Ningún título cumple los filtros seleccionados. Amplía los
    rangos», sin presentar indicadores ni gráficos.

### 9.7.4 Alcance y limitaciones de la validación

La validación funcional y visual de Streamlit se realizó sobre la
aplicación ejecutada localmente con los CSV procesados del proyecto. Se
comprobaron la presentación de los indicadores, las notas de contexto,
los detalles de los rankings, la alternancia de métricas del mapa y el
manejo del caso de correlación sin variación.

En Power BI se revisó, modificó y comprobó directamente el archivo
`DashBoard_Ejecutivo.pbix` mediante las ocho intervenciones BI01--BI08,
que abarcaron la paleta cromática, los indicadores de popularidad y
calificación, la visualización temporal, los países y géneros, el mapa,
los filtros y las fuentes de datos.

No se observaron errores visibles en los escenarios documentados. Estas
comprobaciones verifican el funcionamiento observado con los datos y
escenarios revisados, pero no constituyen una auditoría independiente ni
una validación exhaustiva de todos los cálculos y combinaciones de
filtros.

El escenario de correlación no calculable se comprobó mediante una
selección con calificación constante. No se probó por separado el caso
con menos de dos observaciones.

Con los datos y filtros revisados no se presentó ningún país que
cumpliera el mínimo de títulos con votos y careciera de código ISO-3.
Ese escenario se registra como no observado, sin atribuirle una prueba
que no se realizó.

### 9.7.5 Resultado general de la evaluación

La evaluación crítica permitió fortalecer la solución integral de
StreamView Analytics mediante ajustes en Power BI, Streamlit y la
narrativa visual. Se corrigieron inconsistencias metodológicas en los
indicadores de calificación, se unificó la identidad cromática, se
incorporaron advertencias sobre las limitaciones de los datos y se
mejoró la interpretación de las métricas financieras y geográficas.

Las comprobaciones documentadas confirman la implementación de las
mejoras y su funcionamiento en los escenarios revisados. Sin embargo,
permanecen limitaciones estructurales relacionadas con la cobertura
financiera parcial, la ausencia de votos en determinados títulos y el
carácter estratificado de la extracción.

Por consiguiente, la solución final presenta mayor consistencia
metodológica, claridad comunicacional y utilidad para apoyar decisiones
estratégicas y tácticas, sin atribuir a los datos capacidades
explicativas que no poseen.
