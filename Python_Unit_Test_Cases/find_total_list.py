import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import find_total_recursion
class testas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(find_total_recursion.find_total([1,[1,2],[3,4,5]]),16)


if __name__=="__main__":
    unittest.main()
