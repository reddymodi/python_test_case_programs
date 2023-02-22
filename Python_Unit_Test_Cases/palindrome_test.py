import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import Check_if_Palindrome
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(Check_if_Palindrome.palindrome("121"))

if __name__=="__main__":
    unittest.main()
