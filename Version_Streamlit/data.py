import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
from pathlib import Path
import streamlit as st


def datos_armas(path):

    if os.path.isdir(path):
        all_files = glob.glob(os.path.join(path, "*.csv"))
        if not all_files:
            raise FileNotFoundError(f"No CSV files found in directory: {path}")
        path = all_files[0]
    
    frame = pd.read_csv(path, index_col=None, header=0)
    frame2 = frame.drop(['a', 'b', 'c'], axis=1, errors='ignore')
    
    return(frame2)


def datos_pib(path2):

    if os.path.isdir(path2):
        all_files = glob.glob(os.path.join(path2, "*.csv"))
        if not all_files:
            raise FileNotFoundError(f"No CSV files found in directory: {path2}")
        path2 = all_files[0]
    
    pib = pd.read_csv(path2, index_col=None, header=0)
    frame2 = pib.drop(['a'], axis=1, errors='ignore')
    
    return(frame2)

# def datos_pages(path2):

#     if os.path.isdir(path2):
#         all_files = glob.glob(os.path.join(path2, "*.py"))
#         if not all_files:
#             raise FileNotFoundError(f"No Python files found in directory: {path2}")
#         path2 = all_files[0]
        
#     return(all_files)

# path = r'Version_Streamlit/pages'

# all_files=datos_pages(path)

# print(all_files[0])
# print(all_files[1])
# print(all_files[2])
# print(all_files[3])


def tema():

    if st.context.theme.type == "dark":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")


def graf_suppliers(armas):
    tema()
    frame2 = armas.dropna(subset=['Number delivered'])
    supplier_totals = frame2.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False).head(20)

    fig, ax = plt.subplots(figsize=(10,5), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.bar(supplier_totals.index, supplier_totals.values, color="blue")
    ax.set_xticklabels(supplier_totals.index, rotation=45)
    ax.set_title("Top 20 Suministradores de armas")


def graf_recipients(armas):
    tema()
    frame2 = armas.dropna(subset=['Number delivered'])

    recipient_totals = frame2.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False).head(20)

    fig, ax = plt.subplots(figsize=(10,5), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.bar(recipient_totals.index, recipient_totals.values, color="red")
    ax.set_xticklabels(recipient_totals.index, rotation=45)
    ax.set_title("Top 20 Receptores de armas")


def graf_mayor_supplier(armas):
    tema()
    frame2 = armas.dropna(subset=['Number delivered'])

    supplier_totals = frame2.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False)
    top_supplier = supplier_totals.index[0]
    top_value = supplier_totals.iloc[0]

    supplier_data = frame2[frame2['Supplier'] == top_supplier]

    recipient_totals = supplier_data.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False).head(5)

    labels = [top_supplier] + list(recipient_totals.index)
    values = [top_value] + list(recipient_totals.values)

    fig, ax = plt.subplots(figsize=(10,5), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.bar(labels, values, color=['blue', 'red', 'green', 'orange', 'purple'])
    ax.set_xticklabels(labels, rotation=45)
    ax.set_title(f"Mayor Suministrador: {top_supplier} y sus Top 5 Receptores")
    ax.set_ylabel("Número de Armas Entregadas")


def graf_mayor_recipient(armas):
    tema()
    frame2 = armas.dropna(subset=['Number delivered'])

    recipient_totals = frame2.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False)
    top_recipient = recipient_totals.index[0]
    top_value = recipient_totals.iloc[0]

    recipient_data = frame2[frame2['Recipient'] == top_recipient]

    supplier_totals = recipient_data.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False).head(5)

    labels = [top_recipient] + list(supplier_totals.index)
    values = [top_value] + list(supplier_totals.values)

    fig, ax = plt.subplots(figsize=(10,5), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    ax.bar(labels, values, color=colors[:len(labels)])
    ax.set_xticklabels(labels, rotation=45)
    ax.set_title(f"Mayor Receptor: {top_recipient} y sus Top 5 Suministradores")
    ax.set_ylabel("Número de Armas Entregadas")


def graf_arma(armas):
    tema()
    weapons_totals = armas.groupby('Weapon designation')['Number ordered'].sum().sort_values(ascending=False).head(20)
    fig, ax = plt.subplots(figsize=(10,5), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    ax.bar(weapons_totals.index, weapons_totals.values, color="green")
    ax.set_xticklabels(weapons_totals.index, rotation=45)
    ax.set_title("Top 20 Tipos de Armas Entregadas")


def graf_pib(armas, pib, country):
    tema()
    row = pib[pib['Country Name'] == country]
    if row.empty:
        print(f"No data for {country}")
        return
    year_cols = [col for col in pib.columns if col.isdigit()]
    years = [int(col) for col in year_cols]
    values = row[year_cols].values.flatten()
    values = pd.to_numeric(values, errors='coerce')
    
    fig, ax = plt.subplots(figsize=(10,5), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.plot(years, values)
    ax.set_title(f"PIB de {country}")
    ax.set_xlabel("Año")
    ax.set_ylabel("PIB (US$)")


def graf_arms_gdp(armas, pib, country):
    tema()
    country_arms = {
        "Estados Unidos": "United States",
        "Reino Unido": "United Kingdom",
        "Francia": "France",
        "Alemania": "Germany",
        "Rusia": "Russia",
        "China": "China",
        "India": "India",
    }.get(country, country)
    

    arms_filtered = armas[(armas['Supplier'] == country_arms) & armas['Number delivered'].notna()]
    
    arms_by_year = arms_filtered.groupby('Year of order')['Number delivered'].sum()

    arms_by_year = arms_by_year[arms_by_year.index >= 1960]

    pib_row = pib[pib['Country Name'] == country]
    if pib_row.empty:
        print(f"No GDP data for {country}")
        return

    year_cols = [col for col in pib.columns if col.isdigit() and 1960 <= int(col) <= 2024]
    years = [int(col) for col in year_cols]
    gdp_values = pib_row[year_cols].values.flatten()
    gdp_values = pd.to_numeric(gdp_values, errors='coerce')

    fig, ax1 = plt.subplots(figsize=(12,6), facecolor='none')

    ax1.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax1.patch.set_alpha(0.0)

    ax1.plot(years, gdp_values, 'g-', label='PIB')
    ax1.set_xlabel('Año')
    ax1.set_ylabel('PIB (US$ a precios actuales)', color='g')
    ax1.tick_params(axis='y', labelcolor='g')
    
    ax2 = ax1.twinx()
    ax2.plot(arms_by_year.index, arms_by_year.values, 'r-', label='Armas entregadas')
    ax2.set_ylabel('Número de armas entregadas', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    
    plt.title(f'PIB y Distribución de Armas de {country} (1960-2024)')
    plt.grid(True)


def graf_rece_gdp(armas, pib, country):
    tema()
    country_arms = {
        "Estados Unidos": "United States",
        "Reino Unido": "United Kingdom",
        "Francia": "France",
        "Alemania": "Germany",
        "Rusia": "Russia",
        "China": "China",
        "India": "India",
    }.get(country, country)
    

    arms_filtered = armas[(armas['Recipient'] == country_arms) & armas['Number ordered'].notna()]
    
    arms_by_year = arms_filtered.groupby('Year of order')['Number ordered'].sum()

    arms_by_year = arms_by_year[arms_by_year.index >= 1960]

    pib_row = pib[pib['Country Name'] == country]
    if pib_row.empty:
        print(f"No GDP data for {country}")
        return

    year_cols = [col for col in pib.columns if col.isdigit() and 1960 <= int(col) <= 2024]
    years = [int(col) for col in year_cols]
    gdp_values = pib_row[year_cols].values.flatten()
    gdp_values = pd.to_numeric(gdp_values, errors='coerce')

    fig, ax1 = plt.subplots(figsize=(12,6), facecolor='none')

    ax1.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax1.patch.set_alpha(0.0)

    ax1.plot(years, gdp_values, 'g-', label='PIB')
    ax1.set_xlabel('Año')
    ax1.set_ylabel('PIB (US$ a precios actuales)', color='g')
    ax1.tick_params(axis='y', labelcolor='g')
    
    ax2 = ax1.twinx()
    ax2.plot(arms_by_year.index, arms_by_year.values, 'r-', label='Armas ordenadas')
    ax2.set_ylabel('Número de armas ordenadas', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    
    plt.title(f'PIB y Recepción de Armas de {country} (1960-2024)')
    plt.grid(True)