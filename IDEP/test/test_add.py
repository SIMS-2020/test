import unittest
from IDEP.lib import calc

class TestAdd(unittest.TestCase):

    def testAdd(self):
        result = calc.add(1,1)
        self.assertEqual(result,2)

  