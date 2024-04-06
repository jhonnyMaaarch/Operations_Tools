import pandas as pd
import sys

data_source = sys.argv[1]

if data_source.endswith('.csv'):
    df = pd.read_csv(data_source)
else:
    if data_source.endswith('.xlsx'):
        df = pd.read_excel(data_source)


prelim_data_by_column = df.describe()
print(prelim_data_by_column)

# seperate the independent and dependent (target) variables in your data
# equally valid is: X = df.drop('Price', axis=1)
X = df[['ZIP CODE', 'SIZE', 'YEAR']]
Y = df['Price']

#from sklearn.preprocessing import OneHotEncoder, StandardScaler

#X_encoded = pd.get_dummies(X)   

# from the scikit-learn library comes sklearn.model_selection module from 
# where we obtainted the train_test_split function

from sklearn.model_selection import train_test_split

# we use the train_test_spilt function to split the data into training and testing set
# X represents the independent variable and Y, the dependent variable.
# the test_size is set to 0.2 because we want the number of data assigned to test to be 20% of the dataset
# random_state is set to 42 because we want this to be the number that is used to generate random numbers
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# from scikit-learn linear model we import a class or model called LinearRegression
from sklearn.linear_model import LinearRegression

# we initialize a regression model
model = LinearRegression()

# we use the regression model to fit oytr training data
model.fit(x_train, y_train)

#model evaluation
from sklearn.metrics import mean_squared_error
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")


#This is the point where the actual prediction of outcome happens based on trained model

#predicted_outcome = model.predict(data_source)

#print your final prediction here
#print("***predicted future prices***")
#for price in predicted_outcome:
#    print(price)




