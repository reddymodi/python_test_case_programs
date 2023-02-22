import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import dict_multiply
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(dict_multiply.multiply({"a":12, "b":23, "c":45}),12420)

if __name__=="__main__":
    unittest.main()

