import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from data import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp

st.title("Análisis de bases de datos sobre Intercambios de Armas")
st.header("Introducción")
st.text("Este proyecto analiza las bases de datos de la ONU sobre los intercambios de armas a lo largo del tiempo, determinando los principales países involucrados, los tipos de armas más comunes, y la relación entre el crecimiento económico (PIB) y la distribución de armas. A través de visualizaciones interactivas, se busca comprender mejor las dinámicas globales de comercio de armas y su impacto en la economía mundial.")
st.image("armas.jpg", width="stretch")
st.header("Proyecto desarrollado por:")
st.text("Juan Diego Suárez Agualimpia")
st.text("Daniel Hurtado")