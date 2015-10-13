__author__ = 'Tom'
import numpy as np
import pandas as pd
import nltk
import index as i
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def removestopwords(list):
    stop_words = set(stopwords.words("english"))
    return [w for w in list if not w in stop_words]

def tokenizeElementsinDataFrame(DataFrame, SeriesName):
    return [removestopwords(word_tokenize(DataFrame[SeriesName][k])) for k in range(1, len(DataFrame))]


df = i.df

x = pd.DataFrame

x.description = tokenizeElementsinDataFrame(df, 'description')
print(x.description[1])

# x.threehour = df['threehour']
# print('lllllllllllllllllllllllllll')
# print(x.description[1])
# stop_words = set(stopwords.words("english"))
# desc = word_tokenize('my, name isnt the egg a phil')
# print(stop_words)

# filtered_desc = [w for w in desc if not w in stop_words]

# print(filtered_desc)