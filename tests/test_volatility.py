import unittest
import pysentosa.volatility as vo

def fun(x):
    return x + 1

class MyTest2(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)