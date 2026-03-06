import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from data import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp

st.set_page_config(page_title="Análisis de Intercambios de Armas", page_icon=":material/swords:", layout="wide")

st.title("Análisis de bases de datos sobre Intercambios de Armas", text_alignment="center")
st.header("Introducción")
st.text("Este proyecto analiza las bases de datos de la ONU sobre los intercambios de armas a lo largo del tiempo, determinando los principales países involucrados, los tipos de armas más comunes, y la relación entre el crecimiento económico (PIB) y la distribución de armas. A través de visualizaciones interactivas, se busca comprender mejor las dinámicas globales de comercio de armas y su impacto en la economía mundial.")

search_paths = [
    "principal.jpg",
    "../principal.jpg",
    "Version_Streamlit/principal.jpg",
    os.path.join(os.getcwd(), "principal.jpg"),
    os.path.join(os.path.dirname(__file__), "principal.jpg"),
]

image_files = glob.glob("**/principal.jpg", recursive=True)
search_paths.extend(image_files)

image_path = None
for path in search_paths:
    if os.path.exists(path) and os.path.isfile(path):
        image_path = path
        break

if image_path:
    st.image(image_path, width="stretch")
    st.text("Imagen generada por IA", text_alignment="center")
else:
    st.warning(f"⚠️ No se encontró 'principal.jpg'. Ubicaciones buscadas: {', '.join(search_paths[:3])}")
    st.info(f"📁 Directorio actual: {os.getcwd()}")
st.header("Proyecto desarrollado por:")
st.text("Juan Diego Suárez Agualimpia")
st.text("Daniel Hurtado")
