import unittest
import calc 

class TestCalc(unittest.TestCase):

    def testAdd(self):
        result = calc.add(1,1)
        self.assertEqual(result,2)

    def testSub(self):
        result = calc.sub(1,1)
        self.assertEqual(result,0)
    def testMulti(self):
        result = calc.multi(2,5)
        self.assertEqual(result,10)