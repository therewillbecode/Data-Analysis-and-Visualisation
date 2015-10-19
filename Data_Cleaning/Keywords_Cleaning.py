__author__ = 'Tom'
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def removestopwords(list):
    stop_words = set(stopwords.words("english"))
    return [w for w in list if not w in stop_words]


def tokenizeElements(DataFrame, col):   # tokenize elements for given string in col of df
    return [removestopwords(word_tokenize(DataFrame[col][k])) for k in range(1, len(DataFrame))]



