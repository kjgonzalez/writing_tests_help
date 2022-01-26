'''
secondary file to run another set of tests
'''

import unittest
import modulelib as m

class TestModulelib(unittest.TestCase):
    def test_aplusb(self):
        self.assertEqual(m.aplusb(1,2),3)
