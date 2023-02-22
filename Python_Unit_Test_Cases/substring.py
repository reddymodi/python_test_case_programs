import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import SubString_In_both
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(SubString_In_both.common_char(input("enter ur string:"),input("enter ur string:")),"kesvm")

if __name__=="__main__":
    unittest.main()
