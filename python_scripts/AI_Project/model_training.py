import pandas as pd
import sys

# variable is initialized to the input spreadsheet to be processed
data_source = "zillow_generated_data_v2.xlsx"

# function of pandas library (read_excel) is used to read the content of xlsx
# if the file was csv read_csv is used instead.

df = pd.read_excel(data_source)

# prints the first five rows and all columns
print(df.head())
print("#################")

# provides some information about the data that may be insightful
print(df.info())
print("#################")

# breaks down the dataset into mean, count and more analytically detailed factoid
print(df.describe())
print("################")

# converts or displays the entire dataset as a string
#print(df.to_string())
#print("################")

# isnull() function will look into each cell to determine whether there is a vlaue there or not
# if there is a value it initializes to True. The sum() function aggregates all the values and eventually displays
# then. The total number of empty cells under each column is displayed under the respective column.
print(df.isnull().sum())

# splitting dataset into features (x) and target (y)

X = df.drop('price', axis=1)
Y = df['price']

#split the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Choose a regression algorithm and train the model
#from sklearn.linear_model import LinearRegression
#model = LinearRegression()
#model.fit(X_train, y_train)


# Evaluate model performance
#from sklearn.metrics import mean_squared_error
#y_pred = model.predict(X_test)
#mse = mean_squared_error(y_test, y_pred)

#print(f"Mean Squared  Error: {mse}")


