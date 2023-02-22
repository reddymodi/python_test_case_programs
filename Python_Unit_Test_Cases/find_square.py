import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import first_num_second_num_is_Square
class testas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(first_num_second_num_is_Square.square_num(5),((1,1), (2,4), (3,9), (4,16), (5,25)))

if __name__=="__main__":
    unittest.main()

