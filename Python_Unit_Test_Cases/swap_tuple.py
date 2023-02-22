import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Swap_Tuple
class Testas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Swap_Tuple.swwap((1,2),(3,4)),((3,4),(1,2)))

if __name__=="__main__":
    unittest.main()
