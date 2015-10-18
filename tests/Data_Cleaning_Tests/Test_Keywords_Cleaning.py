__author__ = 'Tom'
__author__ = 'Tom'
import unittest
import pandas as pd
from Data_Cleaning import Keywords_Cleaning as v

df = pd.DataFrame({'description': ['for', 'cat', ' a', 'nettle', 'four']})


class test_removestopwords(unittest.TestCase):

        def test_num_raises_valueerror(self):
            self.assertRaises(TypeError, v.num('qwerty'))


class test_tokenize_elements(unittest.TestCase):

        def test_num_raises_valueerror(self):
            self.assertRaises(TypeError, v.num('qwerty'))

