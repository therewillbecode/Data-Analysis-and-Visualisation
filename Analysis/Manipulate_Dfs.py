__author__ = 'Tom'
import unittest
import pandas as pd
import numpy as np


# mock data frame for tests
df = pd.DataFrame({
                   'country': ['UK', 'FRA', 'UK', 'DE', 'BRA', 'KE'],
                   'pop': [0, 1, 0, 1, 1, 1],
                   'goal': [2, 4, 6, 2, 5, 7],
                   'raised': [0, 2, 1, 4, 5, 7],
                  })


def add_amount_needed(df, goalCol, raisedCol):  # returns DataFrame
    goalCol = str(goalCol)
    raisedCol = str(raisedCol)
    try:
        df['amount_needed'] = df[goalCol] - df[raisedCol]
        return df
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')


def get_unique_vals(df, col):   # returns ndarray of unique vals in df[col]
    col = str(col)
    try:
        return pd.unique(df[col])
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')


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