import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from data import datos_armas, datos_pib, graf_suppliers, graf_recipients, graf_mayor_supplier, graf_mayor_recipient, graf_arma, graf_pib, graf_arms_gdp

path=r'Datos'
path2=r'PIB'
armas= datos_armas(path)
pib= datos_pib(path2)
# print(armas.head(10))   
# print(pib.head(10))

# graf_arms_gdp(armas, pib, "Estados Unidos")