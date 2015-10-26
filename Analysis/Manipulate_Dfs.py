__author__ = 'Tom'
__doc__ = """
Creates new columns for Pandas DataFrames based on existing columns
"""

import unittest
import pandas as pd


# mock data frame for tests
df = pd.DataFrame({
                   'country': ['UK', 'FRA', 'UK', 'DE', 'BRA', 'KE'],
                   'pop': [0, 1, 0, 1, 1, 1],
                   'goal': [2, 4, 6, 2, 5, 7],
                   'raised': [0, 2, 1, 4, 5, 7],
                  })

# Adds column to Pandas DataFrame for amount needed for each project ([goal amount] - [amount raised])
def add_amount_needed(df, goalCol, raisedCol):  # returns DataFrame
    goalCol = str(goalCol)
    raisedCol = str(raisedCol)
    try:
        df['amount_needed'] = df[goalCol] - df[raisedCol]
        return df
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')

def add_amount_needed(df, goalCol, raisedCol):  # returns DataFrame
    goalCol = str(goalCol)
    raisedCol = str(raisedCol)
    try:
        df['amount_needed'] = df[goalCol] - df[raisedCol]
        return df
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')

# returns new NumpyArray which is filtered by 'val' in 'col'
def get_unique_vals(df, col):   # returns ndarray of unique vals in df[col]
    col = str(col)
    try:
        return pd.unique(df[col])
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')

# returns new dataframe which is filtered by 'val' in 'col'
def filter_by_col_val(df, col, val):    # returns DataFrame
    col = str(col)
    try:
        new_df = df[df[col] == val]
        return new_df
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')


l = get_unique_vals(df, 'country')
print(l.__class__.__name__)
print(len(l))
