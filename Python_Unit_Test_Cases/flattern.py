import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import flattern_Use_Recursion
class tesas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(flattern_Use_Recursion.flattern([1,[1,2],[1,2,3,4,[5]]]),[1, 1, 2, 1, 2, 3, 4, 5])
if __name__=="__main__":
    unittest.main() 
