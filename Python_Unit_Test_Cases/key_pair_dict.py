import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import add_key_pair
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(add_key_pair.dict_key({"a":12, "b":23, "c":45}),{"a":12, "b":23, "c":45, "e":42})

if __name__=="__main__":
    unittest.main()


