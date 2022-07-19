from calc_app.calc_app import CalcApp
from mat.cal_funcs import *
import unittest

class TestCalcApp(unittest.TestCase):
    app = CalcApp()

    def test_init(self):
        app = CalcApp()
        self.assertIsInstance(app, CalcApp)
    
    def test_new_calculation(self):
        app = CalcApp()
        c = app.new_calculation("add 1 2")
        self.assertEqual(c, 3)
        c = app.new_calculation("sub 1 4 5 -5 -4")
        self.assertEqual(c, 1)
        c = app.new_calculation("mul 1 3 5 .5")
        self.assertEqual(c, 7.5)
        c = app.new_calculation("div 3 3 3")
        self.assertEqual(c, 1/3)
        c = app.new_calculation("abs -3")
        self.assertEqual(c, "3.0")
        c = app.new_calculation("abs -3 -4")
        self.assertEqual(c, "3.0 4.0")