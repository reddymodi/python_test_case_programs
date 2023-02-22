import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import less_dict_value
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(less_dict_value.less_d({"A":3, "b":1, "c":2,"d":5, "l":4, "m":9}),{'m': 9, 'd': 5, 'l': 4, 'A': 3, 'c': 2, 'b': 1})

if __name__=="__main__":
    unittest.main()


