import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Find_Sum_Of_List
class Testas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Find_Sum_Of_List.list_sum([1,2,3,4,5]),15)

if __name__=="__main__":
    unittest.main()
    
