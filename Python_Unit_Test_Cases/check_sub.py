import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import Check_Substring
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(Check_Substring.Check_sub("kesavmodi","modi"))

if __name__=="__main__":
    unittest.main()
