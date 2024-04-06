import pandas as pd
import sys

data_source = "zillow_generated_data_v2.xlsx"

df = pd.read_excel(data_source)

print(df.head())
print("#################")
print(df.info())
print("#################")
print(df.describe())
print("################")
print(df.to_string())
print("################")
print(df.isnull().sum())

# splitting dataset into features (x) and target (y)

X = df.drop('price', axis=1)
Y = df['price']

#split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Choose a regression algorithm and train the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)


# Evaluate model performance
from sklearn.metrics import mean_squared_error
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared  Error: {mse}")


