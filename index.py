__author__ = 'Tom'
import numpy as np
import pandas as pd

# returns numpy array of unique items for vector column given by index
def getUniqueIndexVals(DataFrame, index):
    if DataFrame.__class__.__name__ != 'DataFrame':
        raise TypeError('arg1 must be an instance of DataFrame Class')
    if isinstance(index, str) == False:
        raise TypeError('arg2 must be String')

    return DataFrame[index].unique()

def filterByType(obj, type):
    if hasattr(obj, '__iter__') == False:
        raise TypeError('arg1 must be an iterable object')
    if isinstance(type, str) == False:
        raise TypeError('arg2 must be String')


RawFrame = pd.read_csv('raw_data.csv', index_col=0, encoding="ISO-8859-1", parse_dates=True)

Nepal = RawFrame[RawFrame.country == 'Nepal'].amount_raised.sum()
Phillipines = RawFrame[RawFrame.country == 'Phillipines']
print(type('country'))
print(RawFrame.__class__.__name__)
print(getUniqueIndexVals(RawFrame, "country"))



