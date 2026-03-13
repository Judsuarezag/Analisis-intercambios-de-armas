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


def tema():

    tema_actual = darkdetect.theme()

    if tema_actual == "Dark":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")



def graf_suppliers(armas,frame_grafico):
    
    tema()

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    frame2 = armas.dropna(subset=['Number delivered'])

    supplier_totals = frame2.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False).head(20)
    
    fig, ax = plt.subplots(figsize=(10,4), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.bar(supplier_totals.index, supplier_totals.values, color="blue")
    ax.set_xticklabels(supplier_totals.index, rotation=35)
    ax.set_title("Top 20 Suministradores de armas")

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)



def graf_recipients(armas,frame_grafico):

    tema()

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    frame2 = armas.dropna(subset=['Number delivered'])

    recipient_totals = frame2.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False).head(20)
    
    fig, ax = plt.subplots(figsize=(10,4), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.bar(recipient_totals.index, recipient_totals.values, color="red")
    ax.set_xticklabels(recipient_totals.index, rotation=35)
    ax.set_title("Top 20 Receptores de armas")

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)



def graf_mayor_supplier(armas,frame_grafico):

    tema()

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    frame2 = armas.dropna(subset=['Number delivered'])

    supplier_totals = frame2.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False)
    top_supplier = supplier_totals.index[0]
    top_value = supplier_totals.iloc[0]

    supplier_data = frame2[frame2['Supplier'] == top_supplier]

    recipient_totals = supplier_data.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False).head(5)

    labels = [top_supplier] + list(recipient_totals.index)
    values = [top_value] + list(recipient_totals.values)

    fig, ax = plt.subplots(figsize=(10,4), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.bar(labels, values, color=['blue', 'red', 'green', 'orange', 'purple'])
    ax.set_xticklabels(labels, rotation=35)
    ax.set_title(f"Mayor Suministrador: {top_supplier} y sus Top 5 Receptores")
    ax.set_ylabel("Número de Armas Entregadas")

    # plt.show()

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)



def graf_mayor_recipient(armas,frame_grafico):

    tema()

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    frame2 = armas.dropna(subset=['Number delivered'])

    recipient_totals = frame2.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False)
    top_recipient = recipient_totals.index[0]
    top_value = recipient_totals.iloc[0]

    recipient_data = frame2[frame2['Recipient'] == top_recipient]

    supplier_totals = recipient_data.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False).head(5)

    labels = [top_recipient] + list(supplier_totals.index)
    values = [top_value] + list(supplier_totals.values)

    fig, ax = plt.subplots(figsize=(10,4), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    colors = ['blue', 'red', 'green', 'orange', 'purple']
    ax.bar(labels, values, color=colors[:len(labels)])
    ax.set_xticklabels(labels, rotation=35)
    ax.set_title(f"Mayor Receptor: {top_recipient} y sus Top 5 Suministradores")
    ax.set_ylabel("Número de Armas Entregadas")

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)



def graf_arma(armas, frame_grafico):

    tema()

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    # frame2 = armas.dropna(subset=['Number delivered'])

    weapons_totals = armas.groupby('Weapon designation')['Number delivered'].sum().sort_values(ascending=False).head(20)

    fig, ax = plt.subplots(figsize=(10,4), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.bar(weapons_totals.index, weapons_totals.values, color="green")
    ax.set_xticklabels(weapons_totals.index, rotation=35)
    ax.set_title("Top 20 Tipos de Armas Entregadas")
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)



def graf_pib(armas, pib, country, frame_grafico):

    tema()

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    row = pib[pib['Country Name'] == country]
    if row.empty:
        print(f"No data for {country}")
        return
    year_cols = [col for col in pib.columns if col.isdigit()]
    years = [int(col) for col in year_cols]
    values = row[year_cols].values.flatten()
    values = pd.to_numeric(values, errors='coerce')

    fig, ax = plt.subplots(figsize=(10,4), facecolor='none')
    ax.set_facecolor('none')
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)

    ax.plot(years, values)
    ax.set_title(f"PIB de {country}")
    ax.set_xlabel("Año")
    ax.set_ylabel("PIB (US$)")

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)



def graf_arms_gdp(arms_df, pib_df, country, frame_grafico):

    tema()

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    country_arms = {
        "Estados Unidos": "United States",
        "Reino Unido": "United Kingdom",
        "Francia": "France",
        "Alemania": "Germany",
        "Rusia": "Russia",
        "China": "China",
        "India": "India",
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

    fig, ax1 = plt.subplots(figsize=(12,4), facecolor='none')
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

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)



def graf_rece_gdp(armas, pib, country, frame_grafico):

    tema()

    for widget in frame_grafico.winfo_children():
            widget.destroy()

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

    fig, ax1 = plt.subplots(figsize=(12,4), facecolor='none')
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

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)