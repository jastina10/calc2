"""Testing File for CSV Functionality"""
import pandas as pd
from addition import Addition


file = pd.read_csv('tests/data/addition.csv')

for index, row in file.iterrows():
    mynumbers = (row['value_1'], row['value_2'])
    print(mynumbers)

df = pd.DataFrame()
print("BEFORE:")
print(df)

for index, row in file.iterrows():
    df['value_1'] = row['value_1']
    df['value_2'] = row['value_2']
    mynumbers = (row['value_1'], row['value_2'])
    addition = Addition(mynumbers)
    df['result'] = addition.get_result()


print("AFTER:")
print(df)


