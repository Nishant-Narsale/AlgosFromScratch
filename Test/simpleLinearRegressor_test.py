from ..simpleLinearRegressor import SimpleLinearRegressor
import pandas as pd

data = pd.read_csv("../datasets/placement.csv")
X = data.iloc[:, 0].values
y = data.iloc[:, 1].values
X_train = X[:150]
y_train = y[:150]
X_test = X[150:]
y_test = y[150:]
slr = SimpleLinearRegressor()
slr.fit(X_train, y_train)
predictions = slr.predict(X_test)

for ct in range(len(X_test)):
    print(X_test[ct], "=>", predictions[ct])