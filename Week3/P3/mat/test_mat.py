from mat.cal_funcs import CalcFuncs
import unittest

class TestMath(unittest.TestCase):
    calc_f = CalcFuncs

    def test_add(self):
        self.assertEqual(self.calc_f.add(1, 2), 3)
        self.assertEqual(self.calc_f.add(1.5, -2, 4), 3.5)
    
    def test_sub(self):
        self.assertEqual(self.calc_f.sub(2, 1), 1)
        self.assertEqual(self.calc_f.sub(1, 2), -1)
        self.assertEqual(self.calc_f.sub(-2, 1.5, -3), -.5)


    def test_mul(self):
        self.assertEqual(self.calc_f.mul(2,3), 6)
        self.assertEqual(self.calc_f.mul(2, 3, .5), 3)
        self.assertEqual(self.calc_f.mul(2, 3, .5), 3)

    
    def test_div(self):
        self.assertEqual(self.calc_f.div(100, 2), 50)
        self.assertEqual(self.calc_f.div(100, 2, 2), 25)
        self.assertEqual(self.calc_f.div(10, -2, 2, .5, 100), -.05)