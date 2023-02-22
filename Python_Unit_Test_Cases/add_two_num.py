import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import add_two_num_test
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(add_two_num_test.add(5,4),9)

if __name__=="__main__":
    unittest.main()
