import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Find_Repeat_Items_Tiple
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Find_Repeat_Items_Tiple.find_rep(tuple(input("enter ur tp:").split())),['2','5','6','7'])

if __name__=="__main__":
    unittest.main()

