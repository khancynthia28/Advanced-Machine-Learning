import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

data = pd.read_csv("EPL17_18.csv")

data_train = data.sample(n = 10)
data_test = data.loc[~data.index.isin(data_train.index)]

X = pd.DataFrame(data['AvgMarketValue'])
y = pd.DataFrame(data['Points'])

X_train = pd.DataFrame(data_train['AvgMarketValue'])
y_train = pd.DataFrame(data_train['Points'])

X_test = pd.DataFrame(data_test['AvgMarketValue'])
y_test = pd.DataFrame(data_test['Points'])

# plot original data
plt.scatter(X,y, color='black')
plt.show()
plt.savefig('graph4.png')

# establish modelling technique
lm = linear_model.LinearRegression()

# fit the model using the first 10 rows!
model = lm.fit(X_train,y_train)

# make predictions from our X variable using last 10 rows!
predictions = lm.predict(X_test)

# plot prediction
plt.scatter(X_test, predictions, color='red') 
plt.show()
#plt.savefig('graph5.png')

# plot real data from last 10 rows
plt.scatter(X_test, y_test, color='green') 
plt.show()
#plt.savefig('graph6.png')

# plot real vs prediction
plt.scatter(y_test, predictions, color='blue')
plt.show()

plt.scatter(X_test, y_test)
plt.plot(X_test, predictions, color='red')
plt.show()