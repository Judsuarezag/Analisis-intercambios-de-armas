import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

def dataframe(path):

    all_files = glob.glob(os.path.join(path + "/*.csv"))

    data = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        data.append(df)

    frame = pd.concat(data, axis=0, ignore_index=True)

    frame2=frame.drop(['a', 'b', 'c'], axis=1)

    return(frame2)

path=r'Datos'
frame2= dataframe(path)
# print(frame2.head(10))

def graf_suppliers(frame2):
    cuenta_suppliers=frame2["Supplier"].value_counts().head(20)
    plt.figure(figsize=(10,5))
    plt.bar(cuenta_suppliers.index, cuenta_suppliers.values, color="blue")
    plt.xticks(rotation=90)
    plt.title("Top 20 Suministradores de armas")
    return plt.show()

# graf_suppliers(frame2)

def graf_recipients(frame2):
    cuenta_recipients=frame2["Recipient"].value_counts().head(20)
    plt.figure(figsize=(10,5))
    plt.bar(cuenta_recipients.index, cuenta_recipients.values, color="red")
    plt.xticks(rotation=90)
    plt.title("Top 20 Receptores de armas")
    return plt.show()

# graf_recipients(frame2)

def graf_mayor_supplier_top_recipients(frame2):
    # Filtrar filas con Number delivered válido
    frame2 = frame2.dropna(subset=['Number delivered'])
    
    # Encontrar el mayor suministrador por suma de Number delivered
    supplier_totals = frame2.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False)
    top_supplier = supplier_totals.index[0]
    top_value = supplier_totals.iloc[0]
    
    # Filtrar datos para el top supplier
    supplier_data = frame2[frame2['Supplier'] == top_supplier]
    
    # Encontrar los 2 países a los que más les suministra
    recipient_totals = supplier_data.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False).head(2)
    
    # Preparar datos para gráfica
    labels = [top_supplier] + list(recipient_totals.index)
    values = [top_value] + list(recipient_totals.values)
    
    # Graficar
    plt.figure(figsize=(8,5))
    plt.bar(labels, values, color=['blue', 'red', 'green'])
    plt.xticks(rotation=45)
    plt.title(f"Mayor Suministrador: {top_supplier} y sus Top 2 Receptores")
    plt.ylabel("Número de Armas Entregadas")
    plt.show()

graf_mayor_supplier_top_recipients(frame2)

