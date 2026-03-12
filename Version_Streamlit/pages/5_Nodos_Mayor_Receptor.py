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

st.title("Análisis del Mayor Receptor de Armas")
st.header("Mayor Receptor de Armas y sus Top 5 Suministradores")
st.text("Este gráfico muestra el mayor receptor de armas en el período analizado, junto con sus 5 principales suministradores. Permite visualizar la relación entre el mayor receptor y los países que más armas le suministran.")
graf_mayor_recipient(armas)
st.pyplot(plt)