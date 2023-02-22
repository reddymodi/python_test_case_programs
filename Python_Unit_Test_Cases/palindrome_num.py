import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import palindrome_test
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(palindrome_test.palindrome("121"),True)

if __name__=="__main__":
    unittest.main()
