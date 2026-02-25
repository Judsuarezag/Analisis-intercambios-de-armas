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

st.title("Top 20 Suministradores de Armas")
graf_suppliers(armas)
st.pyplot(plt)