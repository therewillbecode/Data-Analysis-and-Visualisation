__author__ = 'Tom'
import pandas as pd


def rolling_std(pd_Series):
    return pd.rolling_std(pd_Series, 25, min_periods=1)

# adds 'rolling_std' column to df for given index
def add_roll_std(df, index):
    index = str(index)
    newcol = ('roll_std').join(index)
    print(newcol)
    df[df[newcol]] = rolling_std(df)
    return df

# adds 'rolling_std' column to df for given index
#def add_series

# adds 'rolling_std' column to df for given index  then removes outliers by ' df[df['roll_std'] < 20
def outlier_fixing():
    print('g')


l = pd.Series([2,3,4,5,3,2,1,666,22,5,666666,4,3,5,5,5,5,6,7,8,89,9,7,6,56,6,11,33,4,3,56,73453])
print(l)
s = pd.DataFrame
s.testcol = l
print(add_roll_std(s,'testcol'))
