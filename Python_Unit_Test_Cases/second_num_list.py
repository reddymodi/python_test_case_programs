import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import Sort_2nd_Item_Tuple
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(Sort_2nd_Item_Tuple.second_tuple((('a', 23),('b', 37),('c', 11), ('d',29))),(('c',11),('a',23),('d',29),('b',37)))

if __name__=="__main__":
    unittest.main()
