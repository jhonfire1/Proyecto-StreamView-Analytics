# 3. Identificación de la audiencia objetivo y propósito comunicacional

La solución se diseñó para **dos audiencias** con necesidades distintas, por lo que se construyó un dashboard por cada una.

| | Dashboard Ejecutivo | Dashboard Analítico |
|---|---|---|
| **Audiencia** | Directorio y Gerencia General | Gerencia de Contenidos y Adquisición |
| **Herramienta** | Power BI | Python (Streamlit, pandas, Plotly) |
| **Nivel técnico** | Bajo: necesita una lectura rápida | Medio/alto: explora y compara en detalle |
| **Propósito comunicacional** | **Informar**: dar una visión rápida del estado del catálogo | **Explicar y apoyar la decisión**: profundizar en géneros, países, rankings y finanzas |
| **Decisión que apoya** | Inversión y crecimiento del catálogo | Qué adquirir, renovar o producir |
| **Contenido principal** | KPIs, top 10 países, evolución de lanzamientos, treemap de géneros, películas vs series, mapa por país | 5 pestañas: popularidad y calificación, géneros, rankings, países y finanzas, con 6 filtros |

## Por qué dos herramientas
- **Power BI** ofrece mapas, treemaps y tarjetas de KPI de forma nativa y se modifica visualmente sin escribir código: adecuado para una audiencia ejecutiva.
- **Streamlit/Python** permite reutilizar las columnas financieras calculadas en la limpieza y separar con pandas las columnas con varios valores (género, país, reparto, director): adecuado para el análisis detallado.
- Se evaluó D3 y se descartó porque no aportaba ventajas para este encargo y es la opción más lenta de programar.

## Otras audiencias de las recomendaciones
El storytelling dirige recomendaciones también a Marketing, Producto y al equipo de Data & Analytics (ver notebook `03_storytelling`).
