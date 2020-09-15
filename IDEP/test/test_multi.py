import unittest
from IDEP.lib import calc

class TestMulti(unittest.TestCase):

    def testMulti(self):
        result = calc.multi(2,5)
        self.assertEqual(result,10)