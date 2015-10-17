__author__ = 'Tom'
__author__ = 'Tom'
import unittest

from Data_Cleaning import outliers_validation as v


class test_can_handle_strings(unittest.TestCase):
        def test_should_return_true_for_negative_int(self):
            self.assertEqual(v.check_neg_num('-40'), True)


class test_can_handle_boolean_input(unittest.TestCase):
        def test_can_handle_boolean_input(self):
            self.assertEqual(v.check_neg_num(True), False)


class test_can_handle_boolean_input(unittest.TestCase):
        def test_can_handle_boolean_input(self):
            self.assertEqual(v.check_neg_num(True), False)
