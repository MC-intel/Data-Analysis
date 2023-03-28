#Example Data json
data = [
    {
        "location": "New York, NY",
        "size": 2000,
        "bedrooms": 3,
        "price": "500000"
    },
    {
        "location": "Los Angeles, CA",
        "size": 1500,
        "bedrooms": 2,
        "price": "300000"
    },
    {
        "location": "Chicago, IL",
        "size": 1200,
        "bedrooms": 3,
        "price": "400000"
    },
    {
        "location": "Houston, TX",
        "size": 1800,
        "bedrooms": 4,
        "price": "450000"
    },
    {
        "location": "Phoenix, AZ",
        "size": 1600,
        "bedrooms": 3,
        "price": "350000"
    }
]


df = pd.DataFrame(data)
print(df)

# ML Script

import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the data into a pandas dataframe
#df = pd.read_csv("/content/sample_data/california_housing_test.csv")
# Clean and explore the data
df.dropna(inplace=True)
sns.pairplot(df, x_vars=["size", "bedrooms"], y_vars="price", size=5, aspect=0.7)

# Split the data into training and testing sets
X = df[["size", "bedrooms"]]
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build the model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = lr.predict(X_test)

# Evaluate the performance of the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("Mean Absolute Error:", mae)
print("Root Mean Squared Error:", rmse)

#Predict Price of house

# Model must be trained on .csv data NOT example json data
prediction = lr.predict([[10000, 10]])
print(prediction)  # Outputs the predicted price of the house based on sq footage and amount of rooms

# Similar model for stock analysis

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the data into a pandas dataframe
df = pd.read_csv("stock_prices.csv")

# Preprocess the data
df.dropna(inplace=True)
df = (df - df.mean()) / df.std()
X = df[["market_cap", "earnings", "trading_volume"]]
y = df["price"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build the model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = lr.predict(X_test)

# Evaluate the performance of the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean
