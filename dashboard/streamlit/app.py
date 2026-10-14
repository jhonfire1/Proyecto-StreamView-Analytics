"""
StreamView Analytics — Dashboard Analítico (Etapa 2, sin bloque financiero)
Ejecutar:  streamlit run app.py     (desde la carpeta dashboard/streamlit)

PARA MODIFICAR EN VIVO: casi todo lo que la profesora puede pedir está en la
sección 1 (CONFIGURACIÓN): títulos, umbrales, colores y rangos por defecto.
"""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

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

# Colores por tipo de contenido
COLORES_TIPO = {"Movie": "#E50914", "TV Show": "#1F77B4"}
ESCALA_CONTINUA = "Viridis"

# ══════════════════════════════════════════════════════════════════════════════
# 2. CARGA Y PREPARACIÓN DE DATOS
# ══════════════════════════════════════════════════════════════════════════════
RUTA_DATOS = Path(__file__).resolve().parents[2] / "data" / "processed"
SIN_DATO = "Sin dato"

# Nombre del país (tal como viene en los datos) -> código ISO-3 para el mapa
ISO3 = {
    "United States of America": "USA", "Japan": "JPN", "United Kingdom": "GBR", "China": "CHN",
    "South Korea": "KOR", "France": "FRA", "Canada": "CAN", "Germany": "DEU", "India": "IND",
    "Spain": "ESP", "Belgium": "BEL", "Italy": "ITA", "Mexico": "MEX", "Philippines": "PHL",
    "Hong Kong": "HKG", "Australia": "AUS", "Brazil": "BRA", "Russia": "RUS", "Turkey": "TUR",
    "Sweden": "SWE", "Thailand": "THA", "Denmark": "DNK", "Netherlands": "NLD", "Poland": "POL",
    "Ireland": "IRL", "Taiwan": "TWN", "Norway": "NOR", "Egypt": "EGY", "Argentina": "ARG",
    "Chile": "CHL", "Czech Republic": "CZE", "Switzerland": "CHE", "Colombia": "COL",
    "Austria": "AUT", "South Africa": "ZAF", "Finland": "FIN", "Portugal": "PRT",
    "Indonesia": "IDN", "Israel": "ISR", "Greece": "GRC", "New Zealand": "NZL", "Hungary": "HUN",
    "Bulgaria": "BGR", "Luxembourg": "LUX", "Pakistan": "PAK", "Malaysia": "MYS", "Romania": "ROU",
    "Ukraine": "UKR", "Singapore": "SGP", "Serbia": "SRB", "United Arab Emirates": "ARE",
    "Iceland": "ISL", "Slovakia": "SVK", "Iran": "IRN", "Venezuela": "VEN", "Lebanon": "LBN",
    "Morocco": "MAR", "Croatia": "HRV", "Saudi Arabia": "SAU", "Estonia": "EST",
    "Lithuania": "LTU", "Vietnam": "VNM", "Syrian Arab Republic": "SYR", "Peru": "PER",
    "Uruguay": "URY", "Puerto Rico": "PRI", "Georgia": "GEO", "Iraq": "IRQ", "Latvia": "LVA",
    "Malta": "MLT", "Qatar": "QAT", "Slovenia": "SVN", "Dominican Republic": "DOM", "Cuba": "CUB",
    "Nigeria": "NGA", "Tunisia": "TUN", "Jordan": "JOR", "Cambodia": "KHM", "Kazakhstan": "KAZ",
    "Cyprus": "CYP", "Kuwait": "KWT", "Bosnia and Herzegovina": "BIH", "Macedonia": "MKD",
    "Guatemala": "GTM", "Sri Lanka": "LKA", "Mongolia": "MNG", "Bangladesh": "BGD",
    "Algeria": "DZA", "Kenya": "KEN", "Ecuador": "ECU", "Bolivia": "BOL", "Panama": "PAN",
    "Costa Rica": "CRI", "Paraguay": "PRY", "Belarus": "BLR", "Albania": "ALB", "Armenia": "ARM",
    "Azerbaijan": "AZE", "Ghana": "GHA", "Ethiopia": "ETH", "Nepal": "NPL", "Montenegro": "MNE",
    "Jamaica": "JAM", "Palestinian Territory": "PSE", "Afghanistan": "AFG", "Senegal": "SEN",
}


@st.cache_data
def cargar_datos() -> pd.DataFrame:
    """Une películas y series ya limpias (Entrega 1) en un solo DataFrame."""
    peliculas = pd.read_csv(RUTA_DATOS / "netflix_movies_cleaned.csv")
    series = pd.read_csv(RUTA_DATOS / "netflix_tv_cleaned.csv")
    df = pd.concat([peliculas, series], ignore_index=True)
    # Dejamos fuera las columnas financieras: son del bloque de la Etapa 3.
    return df.drop(columns=[c for c in df.columns if c in
                            ("budget", "revenue", "budget_valido", "revenue_valido",
                             "tiene_datos_financieros", "ROI")])


def separar(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Una fila por valor individual de una columna multivalor ('A, B' -> 2 filas)."""
    out = df.assign(**{columna: df[columna].str.split(",")}).explode(columna)
    out[columna] = out[columna].str.strip()
    return out[out[columna].notna() & (out[columna] != "") & (out[columna] != SIN_DATO)]


# ══════════════════════════════════════════════════════════════════════════════
# 3. PÁGINA Y FILTROS (sidebar)
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(page_title=TITULO_APP, page_icon="🎬", layout="wide")
st.title(TITULO_APP)
st.caption("Gerencia de Contenidos y Adquisición · datos limpios de la Entrega 1")

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

tab1, tab2, tab3, tab4 = st.tabs(
    [" Popularidad y calificación", " Géneros", " Rankings", " Países"])

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
    corr = df_votado["vote_average"].corr(df_votado["popularity"], method="spearman")
    st.caption(f"Correlación de Spearman entre calificación y popularidad: **{corr:.2f}** "
               "(cerca de 0 = relación débil). Solo títulos con al menos 1 voto.")

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
    st.caption(f"Se incluyen géneros con al menos {MIN_TITULOS_GENERO} títulos con votos.")

    # Treemap por volumen
    volumen = df_gen.groupby("genres").size().reset_index(name="titulos")
    fig = px.treemap(volumen, path=["genres"], values="titulos", color="titulos",
                     color_continuous_scale=ESCALA_CONTINUA, title=TITULO_TREEMAP)
    st.plotly_chart(fig, width="stretch")

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
        top = (base.groupby(columna)
               .agg(titulos=("title", "count"), calificacion=("vote_average", "mean"))
               .nlargest(TOP_N, "titulos").reset_index())
        fig = px.bar(top.sort_values("titulos"), x="titulos", y=columna, orientation="h",
                     color="calificacion", color_continuous_scale=ESCALA_CONTINUA,
                     labels={"titulos": "Cantidad de títulos", columna: etiqueta,
                             "calificacion": "Calif. prom."},
                     title=titulo)
        col_st.plotly_chart(fig, width="stretch")
    st.caption("Los títulos sin director/reparto informado ('Sin dato') se excluyen de estos rankings.")

with tab4:
    # Mapa coroplético por país (métrica elegible)
    metrica = st.radio("Métrica del mapa", ["Calificación promedio", "Popularidad promedio"],
                       horizontal=True)
    col_metrica = "vote_average" if metrica.startswith("Calif") else "popularity"
    por_pais = (df_pais_votado.groupby("country")
                .agg(titulos=("title", "count"), valor=(col_metrica, "mean"))
                .query("titulos >= @MIN_TITULOS_PAIS").reset_index())
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
    with st.expander("Ver tabla de países"):
        st.dataframe(mapa[["country", "titulos", "valor"]].sort_values("valor", ascending=False)
                     .rename(columns={"country": "País", "titulos": "Títulos", "valor": metrica}),
                     hide_index=True, width="stretch")
