import pandas as pd
import matplotlib.pyplot as plt

# import the grocery_sales.csv file
sales_data = pd.read_csv('grocery_sales.csv')

print(type(sales_data))
# <class 'pandas.core.frame.DataFrame'>


print(sales_data.shape)
# (281, 4)


print(sales_data.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 281 entries, 0 to 280
# Data columns (total 4 columns):
#  #   Column            Non-Null Count  Dtype
# ---  ------            --------------  -----
#  0   customer_id       281 non-null    int64
#  1   transaction_date  281 non-null    object
#  2   transaction_id    281 non-null    int64
#  3   sales             277 non-null    float64
# dtypes: float64(1), int64(2), object(1)
# memory usage: 8.9+ KB


print(sales_data)
#      customer_id transaction_date  transaction_id   sales
# 0             58       2020-09-01    437091488759   29.93
# 1             80       2020-09-01    437092271839   11.50
# 2             41       2020-09-01    437093560410  101.56
# 3             25       2020-09-01    437096216909   83.01
# 4              2       2020-09-01    437096888457     NaN
# ..           ...              ...             ...     ...
# 276           78       2020-09-30    437383301740   84.47
# 277           31       2020-09-30    437386474006    7.99
# 278           98       2020-09-30    437386544614   12.07
# 279          106       2020-09-30    437387687959  159.23
# 280           44       2020-09-30    437389716957   18.35
#
# [281 rows x 4 columns]


# we want to aggregate data by date
# we have NaN values, we need to remedy this


# fill in missing sales values with avg sales
avg_sales = sales_data['sales'].mean()
# 56.127617

sales_data['sales'].fillna(value=avg_sales, inplace=True)
print(sales_data)

# sum sales by day
sales_summary = sales_data.groupby('transaction_date')['sales'].sum()
print(sales_summary)

# plot sales over time
plt.plot(sales_summary)
plt.xticks(rotation=45)
plt.show()
