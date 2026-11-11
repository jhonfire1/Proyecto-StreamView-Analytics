
import sys
from pathlib import Path

# Permite importar el paquete `src` (en la raíz del repo) al ejecutar `streamlit run`.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import pandas as pd
import plotly.express as px
import streamlit as st

from src.utils import COLORES_TIPO, ISO3, formato_usd, separar
from src.utils import cargar_datos as _cargar_datos

# ══════════════════════════════════════════════════════════════════════════════
# 1. CONFIGURACIÓN  (editar aquí: títulos, umbrales, colores)
# ══════════════════════════════════════════════════════════════════════════════
TITULO_APP = "StreamView Analytics — Dashboard Analítico"

# Títulos de cada gráfico
TITULO_SCATTER = "Popularidad vs calificación"
TITULO_BARRAS_POPULARIDAD = "Popularidad promedio por género"
TITULO_BARRAS_CALIFICACION = "Calificación promedio por género"
TITULO_TREEMAP = "Géneros por volumen de títulos"
TITULO_TOP_EVALUADOS = "Top 10 mejor evaluados"
TITULO_TOP_DIRECTORES = "Top 10 directores (por cantidad de títulos)"
TITULO_TOP_ACTORES = "Top 10 actores (por cantidad de títulos)"
TITULO_MAPA = "Mapa por país"

# Umbrales
MIN_VOTOS_TOP = 50          # votos mínimos para entrar al Top 10 mejor evaluados
MIN_TITULOS_PAIS = 5        # títulos mínimos por país para entrar al mapa
MIN_TITULOS_GENERO = 30     # títulos mínimos por género en las barras
TOP_N = 10                  # largo de los rankings

# Filtro de calificación (valor por defecto del slider)
RANGO_CALIFICACION_DEFECTO = (0.0, 10.0)

# Colores por tipo de contenido: la paleta única vive en src/utils.py (COLORES_TIPO),
# importada arriba, para que notebooks, Streamlit y Power BI usen los mismos colores.
ESCALA_CONTINUA = "Viridis"

# ── Bloque financiero (Etapa 3) ──────────────────────────────────────────────
TITULO_FIN_DISPERSION = "Presupuesto vs ingresos"
TITULO_FIN_TOP_INGRESOS = "Top 10 películas por ingresos"
TITULO_FIN_EXITO = "Éxito con presupuesto reducido"

# Nota visible obligatoria: se completa con el conteo en vivo según los filtros
NOTA_FINANCIERA = ("Este análisis financiero solo incluye películas con presupuesto e ingresos "
                   "informados: {n:,} de {total:,} películas filtradas ({pct:.1f}%).")

# "Presupuesto reducido" = percentil más bajo del presupuesto (sobre todas las películas con datos)
PERCENTIL_PRESUPUESTO_REDUCIDO = 0.25
ROI_MINIMO_EXITO = 3.0                 # "éxito" = ingresos de al menos 3 veces el presupuesto...
INGRESOS_MINIMOS_EXITO = 10_000_000    # ...e ingresos de al menos USD 10 M (evita premiar montos mínimos)

RECUPERA = "Recuperó el presupuesto (ROI ≥ 1)"
NO_RECUPERA = "No recuperó el presupuesto (ROI < 1)"
COLORES_RECUPERO = {RECUPERA: "#2CA02C", NO_RECUPERA: "#FF7F0E"}

# ══════════════════════════════════════════════════════════════════════════════
# 2. CARGA Y PREPARACIÓN DE DATOS
# ══════════════════════════════════════════════════════════════════════════════
# Las funciones de datos (cargar_datos, separar, formato_usd), el diccionario ISO3 y la paleta
# están en src/utils.py y se comparten con los notebooks. Aquí solo se agrega el caché de Streamlit.
cargar_datos = st.cache_data(_cargar_datos)


# ══════════════════════════════════════════════════════════════════════════════
# 3. PÁGINA Y FILTROS (sidebar)
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(page_title=TITULO_APP, page_icon="🎬", layout="wide")
st.title(TITULO_APP)
st.caption("Gerencia de Contenidos y Adquisición · datos limpios de la Entrega 1")
st.info(
    "Alcance de los indicadores: la popularidad corresponde a un índice "
    "relativo de TMDB; no representa reproducciones, engagement ni "
    "retención de usuarios en StreamView. La calificación debe "
    "interpretarse junto con la cantidad de votos recibidos."
)
datos = cargar_datos()

st.sidebar.header("Filtros")
tipos = st.sidebar.multiselect("Tipo de contenido", ["Movie", "TV Show"],
                               default=["Movie", "TV Show"])

anio_min, anio_max = int(datos.release_year.min()), int(datos.release_year.max())
rango_anios = st.sidebar.slider("Rango de años de estreno", anio_min, anio_max,
                                (anio_min, anio_max))

rango_calif = st.sidebar.slider("Rango de calificación", 0.0, 10.0,
                                RANGO_CALIFICACION_DEFECTO, step=0.1)

generos_lista = sorted(separar(datos, "genres")["genres"].unique())
generos_sel = st.sidebar.multiselect("Género", generos_lista, placeholder="Todos")

paises_lista = sorted(separar(datos, "country")["country"].unique())
paises_sel = st.sidebar.multiselect("País", paises_lista, placeholder="Todos")

idiomas_lista = sorted(datos["language"].dropna().unique())
idiomas_sel = st.sidebar.multiselect("Idioma", idiomas_lista, placeholder="Todos")

with st.sidebar.expander(" Sobre la clasificación etaria"):
    st.caption(
        "Este filtro no está disponible: la variable no existe en los datos reales "
        "(era un duplicado de `vote_average`, eliminado en la Entrega 1)."
    )

# ── Aplicar filtros ──────────────────────────────────────────────────────────
df = datos[
    datos["type"].isin(tipos)
    & datos["release_year"].between(*rango_anios)
    & datos["vote_average"].between(*rango_calif)
]
if idiomas_sel:
    df = df[df["language"].isin(idiomas_sel)]



def resumen_personas(base: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Cuenta títulos y calcula calificación solo sobre registros con votos."""
    trabajo = base.copy()
    trabajo["calificacion_valida"] = trabajo["vote_average"].where(trabajo["vote_count"].gt(0))
    return (trabajo.groupby(columna)
            .agg(titulos=("title", "count"),
                 titulos_evaluados=("calificacion_valida", "count"),
                 calificacion=("calificacion_valida", "mean"))
            .reset_index())


def contiene_alguno(serie: pd.Series, elegidos: list) -> pd.Series:
    """True si la celda multivalor contiene alguno de los valores elegidos."""
    return serie.apply(lambda s: any(v.strip() in elegidos for v in str(s).split(",")))


if generos_sel:
    df = df[contiene_alguno(df["genres"], generos_sel)]
if paises_sel:
    df = df[contiene_alguno(df["country"], paises_sel)]

if df.empty:
    st.warning("Ningún título cumple los filtros seleccionados. Amplía los rangos.")
    st.stop()

# Calificación 0 con 0 votos significa "sin votos", no "mala": se excluye de promedios.
df_votado = df[df["vote_count"] > 0]

# Tablas con multivalores separados (una fila por género / país / director / actor)
df_gen = separar(df, "genres")
df_gen_votado = separar(df_votado, "genres")
df_pais_votado = separar(df_votado, "country")

# ══════════════════════════════════════════════════════════════════════════════
# 4. KPIs RÁPIDOS
# ══════════════════════════════════════════════════════════════════════════════
k1, k2, k3, k4 = st.columns(4)
k1.metric("Títulos filtrados", f"{len(df):,}")
k2.metric("Popularidad promedio", f"{df['popularity'].mean():,.1f}")
k3.metric("Calificación promedio", f"{df_votado['vote_average'].mean():.2f}" if len(df_votado) else "—")
k4.metric("Títulos con votos", f"{len(df_votado):,}")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [" Popularidad y calificación", " Géneros", " Rankings", " Países", "💰 Finanzas"])

# ══════════════════════════════════════════════════════════════════════════════
# 5. VISUALIZACIONES
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    # Scatter: popularidad vs calificación (tamaño = votos, color = tipo)
    fig = px.scatter(
        df_votado, x="vote_average", y="popularity",
        color="type", size="vote_count", size_max=28, opacity=0.55,
        color_discrete_map=COLORES_TIPO, log_y=True,
        hover_name="title", hover_data={"release_year": True, "vote_count": True},
        labels={"vote_average": "Calificación promedio", "popularity": "Popularidad (escala log)",
                "type": "Tipo", "vote_count": "Votos"},
        title=TITULO_SCATTER,
    )
    st.plotly_chart(fig, width="stretch")
    pares = df_votado[["vote_average", "popularity"]].dropna()
    if len(pares) < 2 or (pares.nunique() < 2).any():
        st.caption("Correlación de Spearman no disponible: se requieren al menos dos "
                   "títulos con datos y variación en ambas variables.")
    else:
        corr = pares["vote_average"].corr(pares["popularity"], method="spearman")
        st.caption(f"Correlación de Spearman: {corr:.2f}, calculada sobre {len(pares):,} "
                   "títulos con votos y datos en ambas variables. Describe una asociación "
                   "monótona, no una relación causal.")

with tab2:
    # Promedios por género (solo géneros con suficientes títulos)
    por_genero = (df_gen_votado.groupby("genres")
                  .agg(titulos=("title", "count"),
                       popularidad=("popularity", "mean"),
                       calificacion=("vote_average", "mean"))
                  .query("titulos >= @MIN_TITULOS_GENERO").reset_index())
    c1, c2 = st.columns(2)
    with c1:
        fig = px.bar(por_genero.sort_values("popularidad"), x="popularidad", y="genres",
                     orientation="h", color="popularidad", color_continuous_scale=ESCALA_CONTINUA,
                     labels={"popularidad": "Popularidad promedio", "genres": "Género"},
                     title=TITULO_BARRAS_POPULARIDAD)
        st.plotly_chart(fig, width="stretch")
    with c2:
        fig = px.bar(por_genero.sort_values("calificacion"), x="calificacion", y="genres",
                     orientation="h", color="calificacion", color_continuous_scale=ESCALA_CONTINUA,
                     labels={"calificacion": "Calificación promedio", "genres": "Género"},
                     title=TITULO_BARRAS_CALIFICACION)
        st.plotly_chart(fig, width="stretch")
    st.caption(f"Ambos promedios utilizan géneros con al menos {MIN_TITULOS_GENERO} títulos con votos. "
               "El KPI general de popularidad incluye todos los títulos filtrados; las poblaciones difieren.")

    # Treemap por volumen
    volumen = df_gen.groupby("genres").size().reset_index(name="titulos")
    fig = px.treemap(volumen, path=["genres"], values="titulos", color="titulos",
                     color_continuous_scale=ESCALA_CONTINUA, title=TITULO_TREEMAP)
    st.plotly_chart(fig, width="stretch")
    st.caption("Un título puede pertenecer a varios géneros; la suma de categorías "
               "no equivale necesariamente al total de títulos únicos.")

with tab3:
    # Top 10 mejor evaluados con umbral mínimo de votos
    top_eval = (df[df["vote_count"] >= MIN_VOTOS_TOP]
                .nlargest(TOP_N, "vote_average")
                [["title", "type", "release_year", "vote_average", "vote_count", "popularity"]])
    fig = px.bar(top_eval.sort_values("vote_average"), x="vote_average", y="title",
                 orientation="h", color="type", color_discrete_map=COLORES_TIPO,
                 hover_data=["release_year", "vote_count"],
                 labels={"vote_average": "Calificación", "title": "", "type": "Tipo"},
                 title=f"{TITULO_TOP_EVALUADOS} (mín. {MIN_VOTOS_TOP} votos)")
    fig.update_xaxes(range=[0, 10])
    st.plotly_chart(fig, width="stretch")

    # Top directores y actores (excluye 'Sin dato')
    c1, c2 = st.columns(2)
    for col_st, columna, titulo, etiqueta in (
        (c1, "director", TITULO_TOP_DIRECTORES, "Director"),
        (c2, "cast", TITULO_TOP_ACTORES, "Actor/actriz"),
    ):
        base = separar(df, columna)
        top = resumen_personas(base, columna).nlargest(TOP_N, "titulos")
        if top.empty:
            col_st.info(f"No hay datos de {etiqueta.lower()} para los filtros actuales.")
            continue
        evaluados = top[top["calificacion"].notna()].sort_values("titulos")
        sin_evaluar = top[top["calificacion"].isna()].sort_values("titulos")
        fig = px.bar(evaluados, x="titulos", y=columna, orientation="h",
                     color="calificacion", color_continuous_scale=ESCALA_CONTINUA,
                     range_color=[0, 10], hover_data=["titulos_evaluados"],
                     labels={"titulos": "Cantidad de títulos", columna: etiqueta,
                             "calificacion": "Calif. con votos",
                             "titulos_evaluados": "Títulos evaluados"}, title=titulo)
        if not sin_evaluar.empty:
            fig.add_bar(x=sin_evaluar["titulos"], y=sin_evaluar[columna],
                        name="Sin evaluaciones", marker_color="#808080",
                        hovertemplate="%{y}<br>Títulos: %{x}<br>Sin evaluaciones<extra></extra>")
        fig.update_yaxes(categoryorder="array",
                         categoryarray=top.sort_values("titulos")[columna].tolist())
        col_st.plotly_chart(fig, width="stretch")
    st.caption("El ranking cuenta todos los títulos con director/reparto informado. "
               "El color promedia únicamente títulos con votos; gris indica ausencia "
               "de evaluaciones. 'Sin dato' se excluye.")

with tab4:
    # Mapa coroplético por país (métrica elegible)
    metrica = st.radio("Métrica del mapa", ["Calificación promedio", "Popularidad promedio"],
                       horizontal=True)
    col_metrica = "vote_average" if metrica.startswith("Calif") else "popularity"
    resumen_paises = (df_pais_votado.groupby("country")
                .agg(titulos=("title", "count"), valor=(col_metrica, "mean"))
                .reset_index())
    por_pais = resumen_paises[resumen_paises["titulos"] >= MIN_TITULOS_PAIS].copy()
    por_pais["iso3"] = por_pais["country"].map(ISO3)
    mapa = por_pais.dropna(subset=["iso3"])
    fig = px.choropleth(mapa, locations="iso3", color="valor", hover_name="country",
                        hover_data={"titulos": True, "iso3": False},
                        color_continuous_scale=ESCALA_CONTINUA,
                        labels={"valor": metrica, "titulos": "Títulos"},
                        title=f"{TITULO_MAPA}: {metrica.lower()}")
    fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
    st.plotly_chart(fig, width="stretch")
    st.caption(f"Solo países con al menos {MIN_TITULOS_PAIS} títulos con votos "
               f"({len(mapa)} países en el mapa).")
    sin_codigo = por_pais[por_pais["iso3"].isna()]
    bajo_umbral = resumen_paises[resumen_paises["titulos"] < MIN_TITULOS_PAIS]
    st.caption("Ambas métricas del mapa utilizan títulos con votos. Países con datos "
               f"por debajo del umbral: {len(bajo_umbral)}. Países que cumplen el umbral "
               f"pero no tienen código ISO-3: {len(sin_codigo)}.")
    if not sin_codigo.empty:
        with st.expander("Países que cumplen el umbral pero no aparecen en el mapa"):
            st.dataframe(sin_codigo[["country", "titulos", "valor"]]
                         .rename(columns={"country": "País", "titulos": "Títulos", "valor": metrica}),
                         hide_index=True, width="stretch")
    if not bajo_umbral.empty:
        with st.expander("Países excluidos por cantidad insuficiente de títulos con votos"):
            st.dataframe(bajo_umbral.rename(columns={"country": "País", "titulos": "Títulos",
                                                     "valor": metrica}),
                         hide_index=True, width="stretch")
    with st.expander("Ver tabla de países"):
        st.dataframe(mapa[["country", "titulos", "valor"]].sort_values("valor", ascending=False)
                     .rename(columns={"country": "País", "titulos": "Títulos", "valor": metrica}),
                     hide_index=True, width="stretch")

# ══════════════════════════════════════════════════════════════════════════════
# 6. BLOQUE FINANCIERO (Etapa 3) — solo películas con presupuesto e ingresos confiables
# ══════════════════════════════════════════════════════════════════════════════
with tab5:
    n_peliculas = int((df["type"] == "Movie").sum())
    # Piso de USD 1.000 en presupuesto e ingresos aplicado en la Entrega 1 (ya viene en el CSV)
    df_fin = df[df["tiene_datos_financieros"] == True].copy()  # noqa: E712

    if n_peliculas == 0:
        st.info("Los datos financieros existen solo para películas. Incluye \"Movie\" en el "
                "filtro de tipo de contenido para ver este análisis.")
    else:
        # Nota visible obligatoria (conteo en vivo)
        st.info(NOTA_FINANCIERA.format(n=len(df_fin), total=n_peliculas,
                                       pct=len(df_fin) / n_peliculas * 100))
        if df_fin.empty:
            st.warning("Ninguna película de los filtros actuales tiene presupuesto e ingresos "
                       "informados. Amplía los filtros.")
        else:
            df_fin["etiqueta"] = df_fin["title"] + " (" + df_fin["release_year"].astype(str) + ")"
            df_fin["recupero"] = df_fin["ROI"].ge(1).map({True: RECUPERA, False: NO_RECUPERA})

            # KPIs financieros
            total_presupuesto = df_fin["budget_valido"].sum()
            total_ingresos = df_fin["revenue_valido"].sum()
            roi_aproximado = total_ingresos / total_presupuesto
            f1, f2, f3, f4 = st.columns(4)
            f1.metric("Presupuesto promedio", formato_usd(df_fin["budget_valido"].mean()))
            f2.metric("Total ingresos", formato_usd(total_ingresos))
            f3.metric("Total presupuesto", formato_usd(total_presupuesto))
            f4.metric("ROI agregado (razón de totales)", f"{roi_aproximado:.2f}x")
            m1, m2 = st.columns(2)
            m1.metric("ROI mediano por película", f"{df_fin['ROI'].median():.2f}x")
            m2.metric("ROI promedio por película", f"{df_fin['ROI'].mean():.2f}x")
            st.caption("El ROI agregado divide las sumas de ingresos y presupuesto; "
                       "el promedio y la mediana resumen las razones individuales. "
                       "Estos múltiplos no representan beneficio neto ni rentabilidad de StreamView. "
                       "La cobertura parcial no garantiza representatividad del catálogo.")
            sin_recuperar = int((df_fin["ROI"] < 1).sum())
            st.caption(f"ROI aproximado = total de ingresos ÷ total de presupuesto. "
                       f"Mediana del ROI por película: {df_fin['ROI'].median():.2f}x. "
                       f"{sin_recuperar:,} de {len(df_fin):,} películas "
                       f"({sin_recuperar / len(df_fin) * 100:.1f}%) no recuperaron su presupuesto (ROI < 1).")

            # Dispersión presupuesto vs ingresos (ejes logarítmicos + línea de equilibrio)
            fig = px.scatter(
                df_fin, x="budget_valido", y="revenue_valido",
                color="recupero", color_discrete_map=COLORES_RECUPERO,
                log_x=True, log_y=True, opacity=0.6,
                hover_name="etiqueta", hover_data={"ROI": ":.2f", "recupero": False},
                labels={"budget_valido": "Presupuesto (USD, escala log)",
                        "revenue_valido": "Ingresos (USD, escala log)", "recupero": ""},
                title=TITULO_FIN_DISPERSION,
            )
            lim_min = float(min(df_fin["budget_valido"].min(), df_fin["revenue_valido"].min()))
            lim_max = float(max(df_fin["budget_valido"].max(), df_fin["revenue_valido"].max()))
            fig.add_scatter(x=[lim_min, lim_max], y=[lim_min, lim_max], mode="lines",
                            name="Ingresos = presupuesto", line=dict(dash="dash", color="gray"),
                            hoverinfo="skip")
            st.plotly_chart(fig, width="stretch")
            st.caption("Sobre la línea punteada: los ingresos informados superan el presupuesto de producción informado. "
                       "Debajo: no recuperó el presupuesto.")

            # Top películas por ingresos
            top_ingresos = df_fin.nlargest(TOP_N, "revenue_valido")
            fig = px.bar(top_ingresos.sort_values("revenue_valido"), x="revenue_valido", y="etiqueta",
                         orientation="h", color="ROI", color_continuous_scale=ESCALA_CONTINUA,
                         hover_data={"budget_valido": ":,.0f", "ROI": ":.2f"},
                         labels={"revenue_valido": "Ingresos (USD)", "etiqueta": "",
                                 "budget_valido": "Presupuesto (USD)"},
                         title=TITULO_FIN_TOP_INGRESOS)
            st.plotly_chart(fig, width="stretch")

            # ¿Qué películas fueron exitosas con presupuestos reducidos?
            # El límite se calcula sobre TODAS las películas con datos (no cambia al filtrar).
            fin_global = datos[datos["tiene_datos_financieros"] == True]  # noqa: E712
            limite_presupuesto = fin_global["budget_valido"].quantile(PERCENTIL_PRESUPUESTO_REDUCIDO)
            reducidos = df_fin[df_fin["budget_valido"] <= limite_presupuesto]
            exitosas = reducidos[(reducidos["ROI"] >= ROI_MINIMO_EXITO)
                                 & (reducidos["revenue_valido"] >= INGRESOS_MINIMOS_EXITO)]
            st.caption(f"Presupuesto reducido = hasta {formato_usd(limite_presupuesto)} "
                       f"(el {PERCENTIL_PRESUPUESTO_REDUCIDO:.0%} más bajo de las películas con datos financieros). "
                       f"Éxito = ROI de al menos {ROI_MINIMO_EXITO:g}x e ingresos de al menos "
                       f"{formato_usd(INGRESOS_MINIMOS_EXITO)}. En los filtros actuales: "
                       f"{len(exitosas):,} de {len(reducidos):,} películas con presupuesto reducido.")
            if exitosas.empty:
                st.info("Ninguna película con presupuesto reducido cumple el criterio de éxito "
                        "con los filtros actuales.")
            else:
                top_exito = exitosas.nlargest(TOP_N, "ROI")
                fig = px.bar(top_exito.sort_values("ROI"), x="ROI", y="etiqueta", orientation="h",
                             color="revenue_valido", color_continuous_scale=ESCALA_CONTINUA,
                             hover_data={"budget_valido": ":,.0f", "revenue_valido": ":,.0f"},
                             labels={"ROI": "ROI (ingresos ÷ presupuesto)", "etiqueta": "",
                                     "revenue_valido": "Ingresos (USD)",
                                     "budget_valido": "Presupuesto (USD)"},
                             title=f"{TITULO_FIN_EXITO} (top {TOP_N} por ROI)")
                st.plotly_chart(fig, width="stretch")
                with st.expander("Ver todas las películas exitosas con presupuesto reducido"):
                    st.dataframe(
                        exitosas.sort_values("ROI", ascending=False)
                        [["title", "release_year", "budget_valido", "revenue_valido", "ROI"]]
                        .rename(columns={"title": "Título", "release_year": "Año",
                                         "budget_valido": "Presupuesto (USD)",
                                         "revenue_valido": "Ingresos (USD)"}),
                        hide_index=True, width="stretch")
