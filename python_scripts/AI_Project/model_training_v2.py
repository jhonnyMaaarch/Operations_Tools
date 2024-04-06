import pandas as pd
import sys


data_source = sys.argv[1]

df = pd.read_csv(data_source)

print(df.describe())

