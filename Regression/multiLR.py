# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 07:19:29 2018

@author: Cynthia Khan
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv("EPL17_18.csv")

x = pd.DataFrame(data['AvgAge'])
y = pd.DataFrame(data['ForeignPlayers'])
z = pd.DataFrame(data['Points'])

X = pd.DataFrame(data[['AvgAge','ForeignPlayers']])

lm = linear_model.LinearRegression()

model = lm.fit(X.head(10),z.head(10))

predictions = lm.predict(X.tail(10))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x.tail(10),y.tail(10),predictions, c='r')

ax.set_xlabel('Average Age')
ax.set_ylabel('Foreign Players')
ax.set_zlabel('Points')

plt.show()