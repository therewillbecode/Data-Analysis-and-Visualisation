__author__ = 'Tom'
import unittest
import pandas as pd
import random as r
import validation


def random_choice(testargs):
    return r.choice(testargs)

TestArgs = [r.randrange(-10000000, 10000000), r.random()*100, (r.random()*-100), r.randrange(700),
            'B', 'b', 'dobhnio dobgjudo', 'glrgnkrglknd\gd/rlk332fkbhj', 'UK', '$500', '-$500', 'joe\'s fast run usa']

series = []
[series.append(random_choice(TestArgs)) for x in range(0, 90)]

print(series)

class Testreadcsv(unittest.TestCase):
        def test_readcsv(self):
            x = series
            self.assertEqual(all(x) > 1, True)

