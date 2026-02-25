import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from data import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp

st.title("Análisis de Intercambios de Armas")

path = '../Datos'
path2 = '../PIB'
armas = datos_armas(path)
pib = datos_pib(path2)

st.header("Top 20 Suministradores de Armas")
graf_suppliers(armas)
st.pyplot(plt)

st.header("Top 20 Receptores de Armas")
graf_recipients(armas)
st.pyplot(plt)

st.header("Mayor Suministrador y sus Top 5 Receptores")
graf_mayor_supplier(armas)
st.pyplot(plt)

st.header("Mayor Receptor y sus Top 5 Suministradores")
graf_mayor_recipient(armas)
st.pyplot(plt)

st.header("Top 20 Tipos de Armas Entregadas")
graf_arma(armas)
st.pyplot(plt)

st.header("PIB de un País")
country = st.selectbox("Selecciona un país", pib['Country Name'].unique(), key="pib_country")
graf_pib(armas, pib, country)
st.pyplot(plt)

st.header("PIB y Distribución de Armas")
country_options = ["Estados Unidos"]
selected_country = st.selectbox("Selecciona un país", country_options, key="arms_gdp_country")
graf_arms_gdp(armas, pib, selected_country)
st.pyplot(plt)