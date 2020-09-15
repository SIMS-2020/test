import unittest
from IDEP.lib import calc

class TestSub(unittest.TestCase):
    
    def testSub(self):
        result = calc.sub(1,1)
        self.assertEqual(result,0)
 