import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import dict_exist
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(dict_exist.dict_ex({"a":12, "b":23, "c":45},"c"))

if __name__=="__main__":
    unittest.main()

