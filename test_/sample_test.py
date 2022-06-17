import RBFLayer
import tensorflow as tf
import math
import pandas as pd
import numpy as np
import scipy as sc
import seaborn as sns
import os
import time
import matplotlib.pyplot as plt

from keras.losses import binary_crossentropy
from keras.layers import Dense, Flatten, Layer
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import tensorflow_addons as tfa
from tensorflow.keras.callbacks import EarlyStopping, LambdaCallback
from keras.layers import Layer
from keras import backend as K


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


da1 = df1.drop(columns=['date'])
da1.dropna()
scalar1 = MinMaxScaler(feature_range =(0, 1))
data1_ = scalar1.fit_transform(da1)
data1_X = data1_[:, :-1]
data1_Y = data1_[:, -1]
data1_X

x_train1_, x_test1, y_train1_, y_test1 = train_test_split(data1_X, data1_Y, test_size = 0.2, random_state = 1 )
x_train1, x_val1, y_train1, y_val1 =train_test_split(x_train1_, y_train1_, test_size = 0.25, random_state =2 )
x_val1


model1_1A = Sequential()
model1_1A.add(Dense(128, input_dim = (3)))
model1_1A.add(RBFLayer(64, 0.5))
model1_1A.add(Dense(1, activation='sigmoid', name= 'output'))
model1_1A.summary()


model1_1A.compile(optimizer='adam',
              loss=binary_crossentropy,
              metrics=[
                       tf.keras.metrics.RootMeanSquaredError(),
                       tf.keras.metrics.MeanAbsoluteError(),
                       ])


start_time1_1A = time.time()
history1_1A = model1_1A.fit(x_train1, y_train1, validation_data=(x_val1, y_val1), epochs=50, batch_size=50, verbose=1)
end_time1_1A = time.time()


print("--- %s seconds ---" % (end_time1_1A - start_time1_1A))

y_pred1_1A = model1_1A.predict(x_test1)
metric1_1A = r2_score(y_test1, y_pred1_1A)
metric1_1A

def plot_loss(history1_1A):
  plt.plot(history1_1A.history['loss'], label='loss')
  plt.plot(history1_1A.history['val_loss'], label='val_loss')
  plt.ylim([0, 10])
  plt.xlabel('Epoch')
  plt.ylabel('Error')

plot_loss(history1_1A)

