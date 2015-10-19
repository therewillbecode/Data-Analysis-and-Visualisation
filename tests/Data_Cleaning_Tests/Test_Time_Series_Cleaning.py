__author__ = 'Tom'
__author__ = 'Tom'
import unittest
import pandas as pd
import numpy as np
from Data_Cleaning import outliers_cleaning as v


df=pd.DataFrame({'Data':np.random.normal(size=200)})  #example dataset of normally distributed data.


class test_num_handles_unexpected_input(unittest.TestCase):

        def test_num_raises_valueerror(self):
            self.assertRaises(TypeError, v.num('qwerty'))

class test_stringify_(unittest.TestCase):

        def test_num_raises_valueerror(self):
            self.assertEquals(type(v.stringify(['f', True])), str)
            self.assertEquals(type(v.stringify([65, True])), str)
