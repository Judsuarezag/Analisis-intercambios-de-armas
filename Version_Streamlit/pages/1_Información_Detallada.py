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

armas_por_tipo = armas.groupby('Weapon description')['Number ordered'].sum().sort_values(ascending=False).head(20)

weapons_totals = armas.groupby('Weapon designation')['Number ordered'].sum().sort_values(ascending=False).head(20)


st.title("Información Detallada sobre Intercambio de Armas y PIB")
st.header("Datos de Intercambio de Armas por Tipo")

st.dataframe(armas_por_tipo)


st.header("Datos de Intercambio de Armas por Modelo")

st.dataframe(weapons_totals)


st.header("Datos de PIB por País")

st.dataframe(pib.head(20))


st.header("Datos detallados de Intercambio de Armas")

st.dataframe(armas.head(20))