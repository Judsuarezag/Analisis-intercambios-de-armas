import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from data import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp

st.set_page_config(page_title="Análisis de Intercambios de Armas", page_icon=":airplane:", layout="wide")

path = '../Datos'
path2 = '../PIB'
armas = datos_armas(path)

st.title("Mayores Receptores de Armas")
st.header("Top 20 Receptores de Armas")
st.text("Este gráfico muestra los 20 principales receptores de armas en el período analizado, ordenados por la cantidad total de armas recibidas.")
graf_recipients(armas)
st.pyplot(plt)