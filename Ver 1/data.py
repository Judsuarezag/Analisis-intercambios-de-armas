import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

def data(path):

    all_files = glob.glob(os.path.join(path + "/*.csv"))

    data = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        data.append(df)

    frame = pd.concat(data, axis=0, ignore_index=True)

    frame2=frame.drop(['a', 'b'], axis=1)

    return(frame2)

# path=r'Datos'
# frame2= data(path)
# print(frame2.head(10))