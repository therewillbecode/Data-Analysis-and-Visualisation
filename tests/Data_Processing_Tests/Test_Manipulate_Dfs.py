__author__ = 'Tom'
import unittest
import pandas as pd
import numpy as np
from Analysis import Manipulate_Dfs as v


df=pd.DataFrame({'Data': np.random.normal(size=200)})  #example dataset of normally distributed data.


class test_get_unique_vals(unittest.TestCase):

        def test_if_col_not_exist_keyerror(self):
            self.assertRaises(KeyError, v.get_unique_vals(df, 'qwerty1'))


class test_add_amount_needed(unittest.TestCase):

        def test_if_col_not_exist_keyerror(self):
            self.assertRaises(KeyError, v.add_amount_needed(df, 'qwerty1', 'qwerty2'))


class test_filter_by_col_val(unittest.TestCase):

        def test_if_col_not_exist_keyerror(self):
            self.assertRaises(KeyError, v.filter_by_col_val(df, 'qwerty1', 'qwerty2'))