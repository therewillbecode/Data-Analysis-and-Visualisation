__author__ = 'Tom'
import unittest
import pandas as pd
import numpy as np


def add_amount_needed(df, goalCol, raisedCol):
    try:
        df['amount_needed'] = df[goalCol] - df[raisedCol]
        return df
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')


def get_unique_vals(df, col):
    try:
        return pd.unique(df[col])
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')


def filter_by_col_val(df, col, val):
    try:
        new_df = df[df[col] == val]
        return new_df
    except KeyError as e:
        cause = e.args[0]
        print(cause + ' not a valid column in the dataframe')


