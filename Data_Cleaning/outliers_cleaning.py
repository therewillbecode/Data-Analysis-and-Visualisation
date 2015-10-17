__author__ = 'Tom'
import pandas as pd
import numpy as np

df=pd.DataFrame({'Data':np.random.normal(size=200)})  #example dataset of normally distributed data.

def remove_outliers(df, sd):
    df = df[np.abs(df.Data-df.Data.mean())<=(sd*df.Data.std())] #keep only the ones that are within +3 to -3 standard deviations in the column 'Data'.
    df = df[~(np.abs(df.Data-df.Data.mean())>(sd*df.Data.std()))] #or if you prefer the other way around
    return df


def rolling_std(pd_Series):
    return pd.rolling_std(pd_Series, 25, min_periods=1)

print(df)
print(remove_outliers(df, 3))