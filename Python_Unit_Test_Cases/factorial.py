import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import factorial_test
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(factorial_test.fact(5),120)

if __name__=="__main__":
    unittest.main()

