import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import primenum_test
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(primenum_test.prime_num(7),True)

if __name__=="__main__":
    unittest.main()
