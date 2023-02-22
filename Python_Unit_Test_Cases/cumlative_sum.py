import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import cumulative_sum
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(cumulative_sum.cumlative([1,2,3,4,5]),[1,3,6,10,15])

if __name__=="__main__":
    unittest.main()

