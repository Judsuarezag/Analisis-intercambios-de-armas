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

    frame2 = frame2.dropna(subset=['Number delivered'])

    supplier_totals = frame2.groupby('Supplier')['Number delivered'].sum().sort_values(ascending=False).head(20)
    
    plt.figure(figsize=(10,5))
    plt.bar(supplier_totals.index, supplier_totals.values, color="blue")
    plt.xticks(rotation=90)
    plt.title("Top 20 Suministradores de armas")
    plt.show()

# graf_suppliers(frame2)

def graf_recipients(frame2):

    frame2 = frame2.dropna(subset=['Number delivered'])

    recipient_totals = frame2.groupby('Recipient')['Number delivered'].sum().sort_values(ascending=False).head(20)
    plt.figure(figsize=(10,5))
    plt.bar(recipient_totals.index, recipient_totals.values, color="red")
    plt.xticks(rotation=90)
    plt.title("Top 20 Receptores de armas")
    plt.show()

# graf_recipients(frame2)

def graf_mayor_supplier(frame2):

    frame2 = frame2.dropna(subset=['Number delivered'])

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

# graf_mayor_supplier(frame2)

def graf_mayor_recipient(frame2):

    frame2 = frame2.dropna(subset=['Number delivered'])

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

# graf_mayor_recipient(frame2)

def graf_arma(frame2):

    frame2 = frame2.dropna(subset=['Number delivered'])

    weapons_totals = frame2.groupby('Weapon designation')['Number delivered'].sum().sort_values(ascending=False).head(20)
    plt.figure(figsize=(10,5))
    plt.bar(weapons_totals.index, weapons_totals.values, color="green")
    plt.xticks(rotation=60)
    plt.title("Top 20 Tipos de Armas Entregadas")
    plt.show()

# graf_arma(frame2)