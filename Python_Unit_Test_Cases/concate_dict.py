import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import concate_dict
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(concate_dict.concate({"a":12, "b":23, "c":45},{"e":46, "d":54}),{'a': 12, 'b': 23, 'c': 45, 'e': 46, 'd': 54})

if __name__=="__main__":
    unittest.main()
