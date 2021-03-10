"""
Supervised learning example:
An overview of the scikit-learn library for Machine Learning in Python
"""

import pandas as pd

# importing model type and other useful techniques and eval metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# import raw data
# no preprocessing needed here
data_for_model = pd.read_csv("data_for_model.csv")

# known input and known output
X = data_for_model[["input_var1", "input_var2", "input_var3"]]
y = data_for_model["output_var"]

# splitting our X and y objects into training and test sets
# we specify the ration of this split, 80% train, remaining 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create an object using the class of model
regressor = LinearRegression()

# Train our model (regressor object) using the fit method
# using only training data!
regressor.fit(X_train, y_train)

# Applying the trained model to the test set input variables
# using the predict method
# getting predicted output values
y_pred = regressor.predict(X_test)

# Evaluate the accuracy of the model
# based on difference between predicted output values
# and actual output values for the test set
print(r2_score(y_test, y_pred))
