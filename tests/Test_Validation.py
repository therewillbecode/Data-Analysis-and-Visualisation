__author__ = 'Tom'
import unittest
import pandas as pd
import random as r
import validation


TestArgs = [r.randrange(-10000000, 10000000), r.random()*100, (r.random()*-100),
            'B', 'b', 'dobhnio dobgjudo','glrgnkrglknd\gd/rlk332fkbhj', 'UK', '$500', '-$500','joe\'s fast run usa']

sample = r.choice(TestArgs)

series = pd.Series

[series.append(sample) for x in range(0, r.randrange(0, 90))]
print(series)

class Testreadcsv(unittest.TestCase):
        def test_readcsv(self):
            df = sample
            self.assertEqual(sample > 1, True)

