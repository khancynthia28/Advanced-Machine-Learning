import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv("EPL17_18.csv")

X = pd.DataFrame(data['AvgMarketValue'])
y = pd.DataFrame(data['Points'])


plt.xlabel('Market Values')
plt.ylabel('Points')

#plt.plot(X, predictions, color='red')
plt.plot(X, y)

plt.show()

#plt.scatter(X,y)
#plt.savefig('graph1.png')

#establish modelling technique
lm = linear_model.LinearRegression()

# fit the model using the first 10 rows!
model = lm.fit(X.head(10),y.head(10))

# make predictions from our X variable using last 10 rows!
predictions = lm.predict(X.tail(10))


plt.xlim(1,20)
plt.ylim(30,100)
plt.xlabel('Market Values')
plt.ylabel('Points')

plt.plot(X.tail(10), predictions, color='red')
plt.plot(X, y)

plt.show()