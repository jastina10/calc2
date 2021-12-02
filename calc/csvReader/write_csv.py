"""Function to write CSV"""
import pandas as pd
from calc.calculations.addition import Addition

def writecsv(df_from_read):
    """ write CSV"""
    df = pd.DataFrame(columns=['value_1', 'value_2', 'result'])
    for index, row in df_from_read.iterrows():
        mynumbers = (row['value_1'], row['value_2'])
        addition = Addition(mynumbers)
        df = df.append({'value_1': row['value_1'],
                        'value_2': row['value_2']
                           , 'result': addition.get_result()},
                       ignore_index=True)
    df.to_csv('tests/result/output.csv', mode='a', index=False, header=False)
    print(df)
