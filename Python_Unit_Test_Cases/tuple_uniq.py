import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import tuple_equal
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertFalse(tuple_equal.same((10,10,20,10)))

if __name__=="__main__":
    unittest.main()


