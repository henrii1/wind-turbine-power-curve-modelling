import math
import pandas as pd
import numpy as np
import scipy as sc
import seaborn as sns
import os
import time
import matplotlib.pyplot as plt

data_dir = 'dataset\kelmarsh_02.xlsx'

data1 = pd.read_excel(data_dir)

def outlier_remover(dat, prop, min, max):
    d = dat
    q_low = d[prop].quantile(min)
    q_hi  = d[prop].quantile(max)
    return d[(d[prop] < q_hi) & (d[prop] > q_low)]

# Create Sub-DataFrames
d1 = {}
step = 50
i = 1
for x in range(20, 3100, step):
    d1[i] = data1.iloc[((data1['power']>=x)&((data1['power']<x+step))).values]
    #print(d[i])
    i = i + 1
print("There are in total of {} DataFrames".format(i-1))


d1[61] = data1.iloc[(data1['power']>=2900).values]


# Remove outlier
for x in range(1, 62):
    if x <= 3:
        F = 0.95
    elif ((x > 3) and (x <= 10)):
        F = 0.9
    elif ((x > 10) and (x <= 20)):
        F = 0.92
    elif ((x > 20) and (x < 30)):
        F = 0.96
    else:
        F = 0.985
    d1[x] = outlier_remover(d1[x], 'wind speed', 0.00001, F)