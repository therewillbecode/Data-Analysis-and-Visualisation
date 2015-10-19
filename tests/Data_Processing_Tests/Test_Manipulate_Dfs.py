__author__ = 'Tom'
import unittest
import pandas as pd
import numpy as np
from Analysis import Manipulate_Dfs as v

# mock data frame for tests
df = pd.DataFrame({
                   'country': ['UK', 'FRA', 'UK', 'DE', 'BRA', 'KE'],
                   'pop': [0, 1, 0, 1, 1, 1],
                   'goal': [2, 4, 6, 2, 5, 7],
                   'raised': [0, 2, 1, 4, 5, 7],
                  })


class test_get_unique_vals(unittest.TestCase):

        def test_if_col_not_exist_keyerror(self):
            self.assertRaises(KeyError, v.get_unique_vals(df, 'qwerty1'))

        def test_returns_only_unique_vals(self):
            self.assertEquals(len(v.get_unique_vals(df, 'country')), 5)
            self.assertEquals(len(v.get_unique_vals(df, 'pop')), 2)


class test_add_amount_needed(unittest.TestCase):

        def test_if_col_not_exist_keyerror(self):
            self.assertRaises(KeyError, v.add_amount_needed(df, 'qwerty1', 'qwerty2'))

        def test_amount_needed_calculation_correct(self):
            new_frame = v.add_amount_needed(df, 'goal', 'raised')
            amount_n = new_frame['amount_needed']
            self.assertEquals(amount_n[0], 2)
            self.assertEquals(amount_n[5], 0)

class test_filter_by_col_val(unittest.TestCase):

        def test_if_col_not_exist_keyerror(self):
            self.assertRaises(KeyError, v.filter_by_col_val(df, 'qwerty1', 'qwerty2'))

        def test_returns_only_unique_vals(self):
            self.assertEquals(len(v.filter_by_col_val(df, 'pop', 0)), 2)
