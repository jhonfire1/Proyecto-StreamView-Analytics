# StreamView Analytics — Visual Analytics

Solución de Visual Analytics (dashboards interactivos + narrativas visuales + productos gráficos) que apoya decisiones estratégicas sobre el catálogo audiovisual de StreamView Analytics. Proyecto de la asignatura **ADY1104 Visualización de Datos** (Duoc UC).


---

## Arquitectura

```mermaid
flowchart LR
    A["data/raw<br/>CSV originales"] --> B["Notebook de limpieza<br/>(Entrega 1)"]
    B --> C["data/processed<br/>netflix_movies_cleaned.csv<br/>netflix_tv_cleaned.csv"]
    C --> D["Power BI<br/>Dashboard Ejecutivo"]
    C --> E["Streamlit (Python)<br/>Dashboard Analítico"]
```

Los CSV de `data/processed/` son la **única fuente de datos**. Cada dashboard los lee por separado: Streamlit no lee el archivo `.pbix` ni al revés.

| Dashboard | Audiencia | Herramienta | Por qué esta herramienta |
|---|---|---|---|
| Ejecutivo | Directorio y Gerencia General | **Power BI** | Mapas, treemaps y tarjetas de KPI son visuales nativos, se arma rápido y se modifica visualmente sin código |
| Analítico | Gerencia de Contenidos y Adquisición | **Python (Streamlit, pandas, Plotly)** | Reutiliza directamente las columnas financieras ya calculadas en la Entrega 1 y separa con pandas las columnas con varios valores (género, país, actores, directores) |

Se evaluó D3 y se descartó: no aportaba ventajas para este encargo y es la opción más lenta de programar.

---

## Datos y reglas de negocio (resumen de la Entrega 1)

Fuentes: `netflix_movies_detailed_up_to_2025.csv` y `netflix_tv_shows_detailed_up_to_2025.csv` (~16.000 registros cada una), ya limpiadas.

- **Columnas eliminadas:** `duration` (vacía en películas y constante en series) y `rating` (copia exacta de `vote_average`, no era una clasificación por edad).
- **Duplicados:** 9 `show_id` repetidos en series, se conservó la primera ocurrencia.
- **Nulos de texto:** se rellenaron con "Sin dato" para no perder los datos numéricos de esos títulos.
- **Filtrado financiero:** presupuesto o ingresos en 0 (o menores a USD 1.000) se tratan como dato faltante, no como cero real. Solo **3.523 de 16.000 películas (22,0%)** tienen presupuesto e ingresos confiables.
- **Series:** no tienen columnas financieras en la fuente (Regla de Negocio 3: presupuesto e ingresos son exclusivos de películas).
- **Variables derivadas:** `ROI = ingresos / presupuesto` (solo con datos confiables) y `decada`.

---

## Dashboard Ejecutivo (Power BI)

Objetivo: comprender rápidamente el estado del catálogo y apoyar decisiones de inversión y crecimiento.

- **Modelo de datos:** tabla unificada `Catalogo_completo` (películas + series) y tablas dimensionales `catalog_countries` y `catalog_genres` (valores separados por coma convertidos en filas), relacionadas por `show_id`.
- **KPIs:** total de contenidos, películas, series, idiomas, países, géneros, popularidad promedio y calificación promedio.
- **Visualizaciones:** top 10 países, evolución de lanzamientos por año, treemap de géneros, películas vs series y mapa coroplético de producciones por país.
- **Filtros:** rango de años, género y tipo de contenido.
- **Medidas DAX:** `Total Películas` y `Total Series`.

## Dashboard Analítico (Streamlit)

Objetivo: orientar decisiones de adquisición y renovación de contenidos.

- **Filtros (barra lateral):** tipo de contenido, rango de años de estreno, rango de calificación, género, país e idioma.
- **Cinco pestañas:**
  1. **Popularidad y calificación:** dispersión (tamaño = votos, color = tipo, eje Y logarítmico) y correlación de Spearman.
  2. **Géneros:** barras de popularidad y calificación promedio por género, y treemap por volumen.
  3. **Rankings:** top 10 mejor evaluados (mínimo 50 votos), top 10 directores y top 10 actores.
  4. **Países:** mapa coroplético de calificación o popularidad (mínimo 5 títulos por país).
  5. **Finanzas:** KPIs (presupuesto promedio, total ingresos, total presupuesto, ROI aproximado), dispersión presupuesto vs ingresos, top 10 por ingresos y películas exitosas con presupuesto reducido. Incluye una nota visible con el conteo en vivo de películas incluidas.

Preguntas de negocio que responde:

| Pregunta | Dónde se responde |
|---|---|
| ¿Qué géneros priorizar? | Pestaña Géneros |
| ¿Qué países son oportunidad? | Pestaña Países |
| ¿Qué películas fueron exitosas con presupuestos reducidos? | Pestaña Finanzas, última sección |
| ¿Existe relación entre popularidad y calificación? | Pestaña Popularidad y calificación (correlación de Spearman) |

---

## Cómo ejecutar

**Dashboard Analítico (Streamlit)**, desde la raíz del repositorio (los comandos funcionan igual en Windows, macOS y Linux):

```bash
pip install -r requirements.txt
python -m streamlit run dashboard/streamlit/app.py
```

Si `streamlit` no se reconoce como comando, usar siempre `python -m streamlit`. Si el puerto 8501 está ocupado, Streamlit usa el 8502 (la terminal indica la URL).

**Notebooks** (limpieza, visualización y storytelling), en este orden y abriéndolos desde la carpeta `notebooks/`:

```bash
cd notebooks
jupyter notebook          # abrir y ejecutar 01_limpieza_datos, 02_Visualizacion, 03_storytelling
```

El notebook 01 genera los CSV de `data/processed/`; los notebooks 02 y 03 y el dashboard solo los leen.

**Dashboard Ejecutivo (Power BI):** abrir el archivo `DashBoard_Ejecutivo.pbix` de `dashboard/PowerBi/` con Power BI Desktop (solo Windows). Si Power BI no encuentra los CSV en otro computador: *Inicio → Transformar datos → Configuración de origen de datos → Cambiar origen*, y apuntar a `data/processed/`.



---

## Estructura del repositorio

```
Proyecto-StreamView-Analytics/
├── README.md
├── requirements.txt         # dependencias de todo el proyecto
├── data/
│   ├── raw/                 # CSV originales, sin modificar
│   └── processed/           # CSV limpios (fuente única de los dashboards)
├── notebooks/               # 01 limpieza · 02 visualización · 03 storytelling
├── src/
│   └── utils.py             # código compartido: carga de datos, paleta de colores, ISO-3, formatos
├── dashboard/
│   ├── PowerBi/             # Dashboard Ejecutivo (DashBoard_Ejecutivo.pbix)
│   └── streamlit/           # Dashboard Analítico: app.py, requirements.txt
├── docs/
│   └── informe/             # secciones del informe ejecutivo (borradores en Markdown)
└── images/                  # capturas de los dashboards
```

---

## Flujo de trabajo (GitFlow)

El trabajo se hizo en relevo, con una rama por etapa que se integró a `main` antes de que empezara la siguiente:

| Etapa | Rama | Contenido |
|---|---|---|
| 1 | `feature/dashboard-ejecutivo` | Dashboard Ejecutivo en Power BI |
| 2 | `feature/dashboard-analitico` | Dashboard Analítico en Streamlit (sin bloque financiero) |
| 3 | `feature/dashboard-financiero` | Pestaña Finanzas, integración y documentación |

Cada rama se desarrolló con commits descriptivos y se fusionó a `main`.

---

## Paleta de colores (única para todo el proyecto)

| Elemento | Color | HEX |
|---|---|---|
| Películas | Rojo | `#E50914` |
| Series | Azul | `#1F77B4` |

Definida en `src/utils.py` y usada en los notebooks y en Streamlit. **En Power BI deben usarse estos mismos códigos HEX.**

## Decisiones y limitaciones conocidas

- **Clasificación etaria:** no existe en los datos reales (la columna que parecía serlo era un duplicado de `vote_average`). El filtro pedido para el Dashboard Analítico se omitió a propósito y así se informa dentro del dashboard.
- **Alcance financiero:** el análisis financiero cubre solo películas con presupuesto e ingresos informados (22,0% de las películas). Las series no tienen datos financieros.
- **ROI aproximado:** se calcula como total de ingresos dividido por total de presupuesto (la mediana por película se muestra como dato secundario, porque unos pocos casos extremos inflan el promedio). El ROI nunca es negativo; "no recuperó el presupuesto" significa ROI menor a 1.
- **Presupuesto reducido y éxito:** "presupuesto reducido" es el 25% más bajo del presupuesto entre todas las películas con datos; "éxito" exige ROI de al menos 3 e ingresos de al menos USD 10 millones, para no premiar casos con montos ínfimos. Ambos criterios son editables en la configuración de `app.py`.
- **Calificación 0 con 0 votos:** se interpreta como "sin votos", no como "mala". Se excluye de los promedios y de la dispersión del Dashboard Analítico (4.560 títulos).
- **Columnas con varios valores** (`country`, `genres`, `cast`, `director`): en Streamlit se separan fila por fila y "Sin dato" se excluye de los rankings.
- **Muestra estratificada:** el conjunto de datos tiene exactamente 1.000 películas y 1.000 series por año de estreno (2010-2025; 991 series en 2025 tras eliminar duplicados). Los conteos por año no reflejan el tamaño real del catálogo y el gráfico de evolución temporal es plano por construcción.
- **Mapa de Streamlit:** usa un diccionario de códigos ISO-3 (cubre los países con 5 o más títulos). Un país que no esté en el diccionario no se dibuja.


---

## Equipo

| Persona | Nombre | Rol |
|---|---|---|
| 1 | _[Benjamin Barrera]_ | 
| 2 | _[Patrick Gonzalez]_ | 
| 3 | _[Juan Villegas]_ | 
