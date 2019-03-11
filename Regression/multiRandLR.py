# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:17:00 2018

@author: Cynthia Khan
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv("EPL17_18.csv")

data_train = data.sample(n=10)
data_test = data.loc[~data.index.isin(data_train.index)]

X_train = pd.DataFrame(data_train[['AvgAge','ForeignPlayers']])
x_train = pd.DataFrame(data_train['AvgAge'])
y_train = pd.DataFrame(data_train['ForeignPlayers'])
z_train = pd.DataFrame(data_train['Points'])

X_test = pd.DataFrame(data_test[['AvgAge','ForeignPlayers']])
x_test = pd.DataFrame(data_test['AvgAge'])
y_test = pd.DataFrame(data_test['ForeignPlayers'])
z_test = pd.DataFrame(data_test['Points'])

lm = linear_model.LinearRegression()

model = lm.fit(X_train,z_train)

predictions = lm.predict(X_test)
p = predictions.ravel()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x_test,y_test,z_test, c='b')
ax.plot(x_test, y_test, p, c='r', label="LR predictions")
ax.legend()

ax.set_xlabel('Average Age')
ax.set_ylabel('Foreign Players')
ax.set_zlabel('Points')

plt.show()

plt.plot(x_test, z_test, c='b')
plt.xlabel("Average Age")
plt.ylabel("Total Points")
plt.show()

plt.plot(y_test, z_test, c='r')
plt.xlabel("Number of Foreign Players")
plt.ylabel("Total Points")
plt.show()

