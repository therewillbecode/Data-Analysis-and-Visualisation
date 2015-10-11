__author__ = 'Tom'
import numpy as np
import pandas as pd

# returns numpy array of unique elements within set of label
def getUniqueLabelVals(DataFrame, label):
    if DataFrame.__class__.__name__ != 'DataFrame':
        raise TypeError('arg1 must be an instance of DataFrame Class')
    if isinstance(label, str) == False:
        raise TypeError('arg2 must be String')

    df=DataFrame[label].unique()
    # drop na elements

# reads csv and excludes records with > threshold of NaN
def readCsv(csvfile, encoding, index_col=0, threshold=2, parse_dates=True):
    df = pd.read_csv(csvfile, index_col=index_col, encoding=encoding, parse_dates=parse_dates)
    return df.dropna(thresh=threshold)

RawFrame = pd.read_csv('raw_data.csv', encoding="ISO-8859-1")
Nepal = RawFrame[RawFrame.country == 'Nepal'].amount_raised.sum()
Phillipines = RawFrame[RawFrame.country == 'Phillipines']
print(type('country'))
print(RawFrame.__class__.__name__)
print(getUniqueLabelVals(RawFrame, "country"))


g=readCsv('raw_data.csv', encoding="ISO-8859-1").count()

[print(x) for x in g]
