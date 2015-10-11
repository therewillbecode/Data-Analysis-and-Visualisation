__author__ = 'Tom'
import unittest
import index as main

class TestUnique(unittest.TestCase):

    def test_CheckRaiseTypeError(self):
        with self.assertRaises(TypeError):
            main.GetUniqueIndexVals(7, "country")

    def test_one_plus_one(self):
        assert not 1 + 1 == 3