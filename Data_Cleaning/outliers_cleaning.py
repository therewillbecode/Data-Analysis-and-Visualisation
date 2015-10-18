__author__ = 'Tom'
import pandas as pd
import numpy as np

def num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            print('not a valid int or float')


def stringify(s):
    try:
        return str(s)
    except ValueError:
            print('could not convert to string')


# returns a dataframe with row removed where z-score (col) > sd
def remove_outliers(df, sd, col):
    sd = num(sd)    # convert sd to number
    col = str(col)  # convert column name to string
    try:
         df = df[np.abs(df[col]-df[col].mean()) <= (sd*df[col].std())] #keep only the ones that are within +sd to -sd standard deviations in the column 'Data'.
         return df
    except (TypeError):
         print(TypeError('arg1 must be a DataFrame'))
    except (KeyError):
         print('arg3 given for col is not a valid column in arg1 df')


#def rolling_std(pd_Series):
#    return pd.rolling_std(pd_Series, 25, min_periods=1)


df = pd.DataFrame({'Data':np.random.normal(size=200)})  #example dataset of normally distributed data.

#print(df)
#print(remove_outliers(df, 3))