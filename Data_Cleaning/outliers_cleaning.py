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


# returns a dataframe with outliers for std dev removed
def remove_outliers(df, sd):
    sd = num(sd)
    try:
         df = df[np.abs(df.Data-df.Data.mean()) <= (sd*df.Data.std())] #keep only the ones that are within +sd to -sd standard deviations in the column 'Data'.
         df = df[~(np.abs(df.Data-df.Data.mean()) > (sd*df.Data.std()))] #or if you prefer the other way around
         return df
    except (TypeError, AttributeError):
        print('arg1 must be a DataFrame')



def rolling_std(pd_Series):
    return pd.rolling_std(pd_Series, 25, min_periods=1)


df = pd.DataFrame({'Data':np.random.normal(size=200)})  #example dataset of normally distributed data.

#print(df)
#print(remove_outliers(df, 3))