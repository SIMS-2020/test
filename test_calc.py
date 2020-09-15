import unittest
import calc 

class TestCalc(unittest.TestCase):

    def testAdd(self):
        result = calc.add(1,1)
        self.assertEqual(result,2)

    def testAddsa(self):
        result = calc.add(1,1)
        self.assertEqual(result,2)
    def testAdds(self):
        result = calc.add(1,1)
        self.assertEqual(result,2)