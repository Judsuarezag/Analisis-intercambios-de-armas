import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from data import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp, graf_rece_gdp

path = '../Datos'
path2 = '../PIB'
armas = datos_armas(path)
pib = datos_pib(path2)

country_arms = [
    "Estados Unidos",
    "Reino Unido",
    "Francia",
    "Alemania",
    "Rusia",
    "China",
    "India",
]

st.title("Análisis del crecimiento económico y su relación con la distribución de armas")
st.header("Cruce de Información entre el PIB y la Distribución de Armas")
st.text("Este gráfico muestra la relación entre el PIB de un país y la distribución de armas en el período analizado.")
country_options = country_arms
selected_country = st.selectbox("Selecciona un país", country_options, key="arms_gdp_country")
graf_rece_gdp(armas, pib, selected_country)
st.pyplot(plt)