'''
secondary file to run another set of tests
NOTE: you may name a file without using "test_" at the beginning, but then you must make sure the
    test will be found when new tests are being discovered
'''

import unittest
import modulelib as m

class TestModulelib(unittest.TestCase):
    def test_aplusb(self):
        self.assertEqual(m.aplusb(1,2),3)
