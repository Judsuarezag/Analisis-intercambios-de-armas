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

