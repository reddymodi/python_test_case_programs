import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import armstrongNum_Test
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(armstrongNum_Test.arm(153))

if __name__=="__main__":
    unittest.main()
