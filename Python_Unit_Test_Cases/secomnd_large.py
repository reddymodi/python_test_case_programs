import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import second_largest_num
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(second_largest_num.second_large([4,8,9,29,24]),24)

if __name__=="__main__":
    unittest.main()

