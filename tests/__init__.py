import unittest
import test_pysentosa

import os
import sys

TOP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0,TOP_DIR)

def pysentosa_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_pysentosa)
    return suite