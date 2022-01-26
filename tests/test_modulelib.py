'''
The following will perform one test for each defined function. should any of the three
    assertions in "test_Rect" fail, the entire test is considered a failure. should you prefer to
    breakdown each test but keep the object in memory, use the second form of the class, which also
    makes its own "init" function.
    NOTE: each function MUST have "test_" at the start, otherwise won't be recognized

'''

import unittest
import sys
# sys.path.append('..')
import modulelib as m

# # basic example, without custom "init" method
class TestModulelib(unittest.TestCase):
    def test_aplusb(self):
        self.assertEqual(m.aplusb(1,2),3)
    def test_Rect(self):
        r=m.Rect(3,4)
        self.assertEqual(r.perim,14)
        self.assertEqual(r.area,12)
        self.assertAlmostEqual(r.diag,5.0)

class TestModulelib2(unittest.TestCase):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.rect = m.Rect(3,4)
    def test_aplusb(self):
        self.assertEqual(m.aplusb(4,5),9)
    def test_perim(self):
        self.assertEqual(self.rect.perim,14)
    def test_area(self):
        self.assertEqual(self.rect.area,12)
    def test_diag(self):
        self.assertAlmostEqual(self.rect.diag,5)
