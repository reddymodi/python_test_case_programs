import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Largest_even_odd
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Largest_even_odd.pr_even([2,5,8,9,6]),(8,9))

if __name__=="__main__":
    unittest.main()

