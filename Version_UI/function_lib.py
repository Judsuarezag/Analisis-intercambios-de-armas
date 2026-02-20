import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import darkdetect
import tkinter as tk
from tkinter import ttk
import sv_ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

def datos_armas(path):

    all_files = glob.glob(os.path.join(path + "/*.csv"))

    data = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        data.append(df)

    frame = pd.concat(data, axis=0, ignore_index=True)

    frame2=frame.drop(['a', 'b', 'c'], axis=1)

    return(frame2)

def datos_pib(path2):

    all_files = glob.glob(os.path.join(path2 + "/*.csv"))

    data = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        data.append(df)

    pib = pd.concat(data, axis=0, ignore_index=True)

    frame2=pib.drop(['a'], axis=1)

    pib = frame2.dropna(subset=['Country Name'])

    return(pib)

# path=r'Datos'
# path2=r'PIB'
# armas= datos_armas(path)
# pib= datos_pib(path2)
# print(armas.head(10))   
# print(pib.head(10))

def graf_suppliers(armas,frame_grafico):

    frame2 = armas.dropna(subset=['Number delivered'])

    supplier_totals = frame2.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False).head(20)
    
    plt.figure(figsize=(10,5))
    plt.bar(supplier_totals.index, supplier_totals.values, color="blue")
    plt.xticks(rotation=90)
    plt.title("Top 20 Suministradores de armas")
    plt.show()

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# graf_suppliers(armas)

def graf_recipients(armas,frame_grafico):

    frame2 = armas.dropna(subset=['Number delivered'])

    recipient_totals = frame2.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False).head(20)
    plt.figure(figsize=(10,5))
    plt.bar(recipient_totals.index, recipient_totals.values, color="red")
    plt.xticks(rotation=90)
    plt.title("Top 20 Receptores de armas")
    plt.show()

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# graf_recipients(armas)

def graf_mayor_supplier(armas,frame_grafico):

    frame2 = armas.dropna(subset=['Number delivered'])

    supplier_totals = frame2.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False)
    top_supplier = supplier_totals.index[0]
    top_value = supplier_totals.iloc[0]

    supplier_data = frame2[frame2['Supplier'] == top_supplier]

    recipient_totals = supplier_data.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False).head(5)

    labels = [top_supplier] + list(recipient_totals.index)
    values = [top_value] + list(recipient_totals.values)

    plt.figure(figsize=(10,5))
    plt.bar(labels, values, color=['blue', 'red', 'green', 'orange', 'purple'])
    plt.xticks(rotation=45)
    plt.title(f"Mayor Suministrador: {top_supplier} y sus Top 5 Receptores")
    plt.ylabel("Número de Armas Entregadas")
    plt.show()

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

# graf_mayor_supplier(armas)

def graf_mayor_recipient(armas):

    frame2 = armas.dropna(subset=['Number delivered'])

    recipient_totals = frame2.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False)
    top_recipient = recipient_totals.index[0]
    top_value = recipient_totals.iloc[0]

    recipient_data = frame2[frame2['Recipient'] == top_recipient]

    supplier_totals = recipient_data.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False).head(5)

    labels = [top_recipient] + list(supplier_totals.index)
    values = [top_value] + list(supplier_totals.values)

    plt.figure(figsize=(10,5))
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    plt.bar(labels, values, color=colors[:len(labels)])
    plt.xticks(rotation=45)
    plt.title(f"Mayor Receptor: {top_recipient} y sus Top 5 Suministradores")
    plt.ylabel("Número de Armas Entregadas")
    plt.show()

# graf_mayor_recipient(armas)

def graf_arma(armas):

    frame2 = armas.dropna(subset=['Number delivered'])

    weapons_totals = frame2.groupby('Weapon designation')['Number delivered'].sum().sort_values(ascending=False).head(20)
    plt.figure(figsize=(10,5))
    plt.bar(weapons_totals.index, weapons_totals.values, color="green")
    plt.xticks(rotation=60)
    plt.title("Top 20 Tipos de Armas Entregadas")
    plt.show()

# graf_arma(armas)

def graf_pib(armas, pib, country):

    row = pib[pib['Country Name'] == country]
    if row.empty:
        print(f"No data for {country}")
        return
    year_cols = [col for col in pib.columns if col.isdigit()]
    years = [int(col) for col in year_cols]
    values = row[year_cols].values.flatten()
    values = pd.to_numeric(values, errors='coerce')
    plt.figure(figsize=(10,5))
    plt.plot(years, values)
    plt.title(f"PIB de {country}")
    plt.xlabel("Año")
    plt.ylabel("PIB (US$)")
    plt.show()

def graf_arms_gdp(arms_df, pib_df, country):

    country_arms = {
        "Estados Unidos": "United States",
    }.get(country, country)
    

    arms_filtered = arms_df[(arms_df['Supplier'] == country_arms) & arms_df['Number delivered'].notna()]
    
    arms_by_year = arms_filtered.groupby('Year of order')['Number delivered'].sum()

    arms_by_year = arms_by_year[arms_by_year.index >= 1960]

    pib_row = pib_df[pib_df['Country Name'] == country]
    if pib_row.empty:
        print(f"No GDP data for {country}")
        return

    year_cols = [col for col in pib_df.columns if col.isdigit() and 1960 <= int(col) <= 2024]
    years = [int(col) for col in year_cols]
    gdp_values = pib_row[year_cols].values.flatten()
    gdp_values = pd.to_numeric(gdp_values, errors='coerce')

    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.plot(years, gdp_values, 'b-', label='PIB')
    ax1.set_xlabel('Año')
    ax1.set_ylabel('PIB (US$ a precios actuales)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    
    ax2 = ax1.twinx()
    ax2.plot(arms_by_year.index, arms_by_year.values, 'r-', label='Armas entregadas')
    ax2.set_ylabel('Número de armas entregadas', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    
    plt.title(f'PIB y Distribución de Armas de {country} (1960-2024)')
    plt.grid(True)
    plt.show()

# graf_arms_gdp(armas, pib, "Estados Unidos")