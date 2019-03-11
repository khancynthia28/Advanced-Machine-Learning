import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("EPL17_18.csv")
predictions = []
marketValues = []
points = []

for x in range(20):
    data_train = data.sample(n = 10)
    data_test = data.loc[~data.index.isin(data_train.index)]

    X = pd.DataFrame(data['AvgMarketValue'])
    y = pd.DataFrame(data['Points'])

    X_train = pd.DataFrame(data_train['AvgMarketValue'])
    y_train = pd.DataFrame(data_train['Points'])

    X_test = pd.DataFrame(data_test['AvgMarketValue'])
    y_test = pd.DataFrame(data_test['Points'])

# establish modelling technique
    lm = linear_model.LinearRegression()

# fit the model using the first 10 rows!
    model = lm.fit(X_train,y_train)

# make predictions from our X variable using last 10 rows!
    predictions.append(lm.predict(X_test))
    x_array = np.asarray(X_test)
    y_array = np.asarray(y_test)
    marketValues.append(x_array)
    points.append(y_array)

# take average
avg_predictions = np.mean(predictions, axis=0)
avg_marketValues = np.mean(marketValues, axis=0)
avg_points = np.mean(points, axis=0)
print(avg_predictions)
print(avg_points)
print('Variance score: %.2f' % r2_score(avg_points, avg_predictions))

# plot real vs average
plt.xlabel('Random Average Market Values')
plt.ylabel('Random Average Points')

plt.plot(avg_marketValues, avg_predictions, color='red')
plt.scatter(avg_marketValues, avg_points)

plt.show()