# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 22:12:45 2018

@author: Cynthia Khan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv("EPL17_18.csv")

predictions = []
xaxis = []
yaxis = []
zaxis = []

# repeat 20 times
for x in range(20):
    # sample random rows
    data_train = data.sample(n = 10)
    data_test = data.loc[~data.index.isin(data_train.index)]
    
    X_train = pd.DataFrame(data_train[['AvgAge','ForeignPlayers']])
    x_train = pd.DataFrame(data_train['AvgAge'])
    y_train = pd.DataFrame(data_train['ForeignPlayers'])
    z_train = pd.DataFrame(data_train['Points'])

    X_test = pd.DataFrame(data_test[['AvgAge','ForeignPlayers']])
    x_test = pd.DataFrame(data_test['AvgAge'])
    y_test = pd.DataFrame(data_test['ForeignPlayers'])
    z_test = pd.DataFrame(data_test['Points'])

    # model
    lm = linear_model.LinearRegression()

    model = lm.fit(X_train,z_train)

    # predict
    predictions.append(lm.predict(X_test))
    
    x_array = np.asarray(x_test)
    y_array = np.asarray(y_test)
    z_array = np.asarray(z_test)
    
    xaxis.append(x_array)
    yaxis.append(y_array)
    zaxis.append(z_array)
    
    
# average
avg_predictions = np.mean(predictions, axis=0)
p = avg_predictions.ravel()

avg_x = np.mean(xaxis, axis=0)
avg_y = np.mean(yaxis, axis=0)
avg_z = np.mean(zaxis, axis=0)

# plot
plt.plot(avg_x, avg_z, c='b')
plt.xlabel("Average Age")
plt.ylabel("Average Total Points")
plt.show()

plt.plot(avg_y, avg_z, c='r')
plt.xlabel("Average Number of Foreign Players")
plt.ylabel("Average Total Points")
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(avg_x,avg_y,avg_z, c='b')
ax.plot(avg_x, avg_y, p, c='r', label="LR (avg) predictions")
ax.legend()

ax.set_xlabel('Average Age')
ax.set_ylabel('Average Number of Foreign Players')
ax.set_zlabel('Average Points')

plt.show()