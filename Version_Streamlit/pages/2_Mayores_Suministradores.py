import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from data import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp

st.set_page_config(page_title="Análisis de Intercambios de Armas", page_icon=":material/swords:", layout="wide")

path = "../Datos"
path2 = "../PIB"
armas = datos_armas(path)

st.title("Mayores Suministradores de Armas")
st.header("Top 20 Suministradores de Armas")
st.text("Este gráfico muestra los 20 principales suministradores de armas en el período analizado, ordenados por la cantidad total de armas entregadas.")
graf_suppliers(armas)
st.pyplot(plt)