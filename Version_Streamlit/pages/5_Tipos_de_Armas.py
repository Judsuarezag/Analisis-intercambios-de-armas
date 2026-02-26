import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from data import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp

path = '../Datos'
path2 = '../PIB'
armas = datos_armas(path)

st.title("Análisis de tipos de armas entregadas")
st.header("Tipos de Armas Entregadas")
st.text("Este gráfico muestra los tipos de armas más entregados en el período analizado ordenados por cantidad.")
graf_arma(armas)
st.pyplot(plt)