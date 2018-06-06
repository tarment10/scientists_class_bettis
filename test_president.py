#!/usr/bin/env python
import unittest
import sys
from president import President

class TestPresident(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.pres = President(1)

    @unittest.skipIf(sys.platform == 'win32', 'Not implemented on Windows')
    def test_gw_first_name_george(self):
        self.assertEqual(self.pres.first_name, 'George', '''President 1's first name is not "George"''')

    def test_gw_last_name_washington(self):
        self.assertEqual(self.pres.last_name, 'Washington')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
