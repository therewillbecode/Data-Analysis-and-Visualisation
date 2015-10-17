__author__ = 'Tom'

import pandas as pd
import numpy as np

def basic_stats(df):    # excludes NaN values
    return df.describe()


def pairwise_corr(df):  # Compute pairwise correlation of columns, excluding NA/null values
    return df.corr(method='pearson', min_periods=1)
