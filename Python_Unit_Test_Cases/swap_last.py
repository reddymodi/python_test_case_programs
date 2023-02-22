import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import swap_first_last
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(swap_first_last.swap_list([4,3,2,1,6]),[6,3,2,1,4])

if __name__=="__main__":
    unittest.main()

