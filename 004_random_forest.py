"""
Random Forest example:

Here we build, train, and test our Random Forest model to predict how long it will take
certain video game players to complete a particular challenge in their game,
based on their level and the amount of ammo their character has.
"""

# Import the required Python packages

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd


# Import the dataset

my_df = pd.read_csv("video_game_data.csv")

# print(my_df)
print(my_df.info())

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 30 entries, 0 to 29
# Data columns (total 3 columns):
#  #   Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   level            30 non-null     int64
#  1   ammo             30 non-null     int64
#  2   completion_time  30 non-null     int64
# dtypes: int64(3)
# memory usage: 848.0 bytes
# None

# Split data into input and output objects

X = my_df.drop(["completion_time"], axis=1)

y = my_df["completion_time"]

# Split data into training and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate the model object

regressor = RandomForestRegressor(random_state=42)

# Train the model

regressor.fit(X_train, y_train)

# Assess the accuracy of the model

y_pred = regressor.predict(X_test)

prediction_comparison = pd.DataFrame({"actual": y_test,
                                      "prediction": y_pred})

print(prediction_comparison)

score = r2_score(y_test, y_pred)
print(f"\nAccuracy score: {score}")
