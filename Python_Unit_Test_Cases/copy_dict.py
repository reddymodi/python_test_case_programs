import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import copy_dict
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(copy_dict.cp({"a":3, "b":4, "c":5}),{"a":3, "b":4, "c":5})

if __name__=="__main__":
    unittest.main()
