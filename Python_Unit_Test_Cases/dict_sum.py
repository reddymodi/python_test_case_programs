import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import sum_dict
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(sum_dict.sum_d({"a":12, "b":23, "c":45}),80)

if __name__=="__main__":
    unittest.main()
