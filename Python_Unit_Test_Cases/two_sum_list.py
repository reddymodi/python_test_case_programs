import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import two_list_sum
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(two_list_sum.twossum([2,4,3],[5,6,4]),708)

if __name__=="__main__":
    unittest.main()
