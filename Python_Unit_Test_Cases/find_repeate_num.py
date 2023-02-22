import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import find_num
class testas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(find_num.repeate(list(map(int,input("enter te list:").split()))),{3:2, 1:2, 5:1})

if __name__=="__main__":
    unittest.main()

