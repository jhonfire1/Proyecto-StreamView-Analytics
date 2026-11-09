
from pathlib import Path

import pandas as pd

# ── Rutas ────────────────────────────────────────────────────────────────────
RAIZ = Path(__file__).resolve().parents[1]
RUTA_DATOS = RAIZ / "data" / "processed"

# ── Constantes de datos ──────────────────────────────────────────────────────
SIN_DATO = "Sin dato"

# ── Paleta única ─────────────────────────────────────────────────────────────
# Mismos colores en notebooks, Streamlit y Power BI (en Power BI usar estos códigos HEX).
COLOR_PELICULA = "#E50914"   # rojo
COLOR_SERIE = "#1F77B4"      # azul

COLORES_TIPO = {"Movie": COLOR_PELICULA, "TV Show": COLOR_SERIE}          # columna `type` de los CSV
COLORES_CATALOGO = {"Películas": COLOR_PELICULA, "Series": COLOR_SERIE}  # etiquetas en español (notebooks)

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


# ── Funciones de datos ───────────────────────────────────────────────────────
def cargar_datos() -> pd.DataFrame:
    """Une películas y series ya limpias (Entrega 1) en un solo DataFrame.

    Conserva las columnas financieras (budget_valido, revenue_valido,
    tiene_datos_financieros, ROI): solo las usa la pestaña Finanzas.
    """
    peliculas = pd.read_csv(RUTA_DATOS / "netflix_movies_cleaned.csv")
    series = pd.read_csv(RUTA_DATOS / "netflix_tv_cleaned.csv")
    return pd.concat([peliculas, series], ignore_index=True)


def separar(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """Una fila por valor individual de una columna multivalor ('A, B' -> 2 filas).

    Excluye vacíos y "Sin dato".
    """
    out = df.assign(**{columna: df[columna].str.split(",")}).explode(columna)
    out[columna] = out[columna].str.strip()
    return out[out[columna].notna() & (out[columna] != "") & (out[columna] != SIN_DATO)]


def formato_usd(x: float) -> str:
    """Monto en USD en formato corto: $35.7 M, $367.4 mil M."""
    if abs(x) >= 1e9:
        return f"${x / 1e9:,.1f} mil M"
    if abs(x) >= 1e6:
        return f"${x / 1e6:,.1f} M"
    return f"${x:,.0f}"
