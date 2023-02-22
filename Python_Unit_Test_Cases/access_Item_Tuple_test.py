import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import access_tuple
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(access_tuple.tuple_ch(("Orange", [10, 20, 30], (5, 15, 25))),20)

if __name__=="__main__":
    unittest.main()
