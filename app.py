import sys
sys.path.insert(0, './mi_entorno')
import config

import pyswisseph as swe

# Configura el entorno de Swiss Ephemeris usando la ruta de config.py
swe.set_ephe_path(config.EPHEMERIS_PATH)

# Ejemplo de cómo obtener la posición del Sol
jd = swe.julday(2024, 8, 9)  # Fecha en formato Julian Day
position = swe.calc_ut(jd, swe.SUN)

print("Posición del Sol:", position)
import swisseph as swe
import pandas as pd

# Configura la ruta de Swiss Ephemeris
EPHEMERIS_PATH = 'C:\\Users\\zerin\\Documents\\swisseph'
swe.set_ephe_path(EPHEMERIS_PATH)

# Función para obtener la posición de un cuerpo celeste
def get_planet_position(julian_day, planet):
    position, _ = swe.calc_ut(julian_day, planet)
    return position

# Lista de cuerpos celestes relevantes
planets = {
    'Sun': swe.SUN,
    'Moon': swe.MOON,
    'Mercury': swe.MERCURY,
    'Venus': swe.VENUS,
    'Mars': swe.MARS,
    'Jupiter': swe.JUPITER,
    'Saturn': swe.SATURN,
    'Uranus': swe.URANUS,
    'Neptune': swe.NEPTUNE,
    'Pluto': swe.PLUTO,
    'Chiron': swe.CHIRON,  # Incluye a Quirón
    'Ceres': swe.CERES     # Incluye a Ceres
}

# Función para generar la carta astral
def generate_chart(year, month, day, hour=0, minute=0, second=0):
    jd = swe.julday(year, month, day, hour + minute/60 + second/3600)
    positions = {name: get_planet_position(jd, planet) for name, planet in planets.items()}
    return positions

# Ejemplo de uso:
birth_chart = generate_chart(2024, 8, 11)
df = pd.DataFrame(birth_chart).T  # Crear un DataFrame para una mejor visualización
print(df)
