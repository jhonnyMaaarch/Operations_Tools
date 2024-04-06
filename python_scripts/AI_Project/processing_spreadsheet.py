import pandas as pd

df = pd.read_excel("zillow_generated_data_v2.xlsx")

print(df.head())
print("#######")
print(df.info())
print("#######")
print(df.describe())


