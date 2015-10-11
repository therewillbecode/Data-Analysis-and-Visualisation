__author__ = 'Tom'
import numpy as np
import pandas as pd


def GetUniqueIndexVals(DataFrame, Index):
    if DataFrame.__class__.__name__ != "DataFrame":
        raise TypeError("arg1 must be an instance of DataFrame Class")
    if isinstance(Index, str) == False:
        raise TypeError("arg2 must be String")

    return DataFrame[Index].unique()



RawFrame = pd.read_csv('raw_data.csv', index_col=0, encoding="ISO-8859-1", parse_dates=True)

Nepal = RawFrame[RawFrame.country == 'Nepal'].amount_raised.sum()
Phillipines = RawFrame[RawFrame.country == 'Phillipines']
print(type('country'))
print(RawFrame.__class__.__name__)
print(GetUniqueIndexVals(RawFrame, "country"))



