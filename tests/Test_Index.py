__author__ = 'Tom'
import unittest
import index as main

class TestUnique(unittest.TestCase):

    # check that functions limit arg types
    def test_CheckRaiseTypeError(self):
        with self.assertRaises(TypeError):
            main.getUniqueLabelVals(7, 'country')

    def test_FilterRaisesTypeError(self):
        with self.assertRaises(TypeError):
            main.filterByType(7, 'str')



