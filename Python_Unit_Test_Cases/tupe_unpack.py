import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Tuple_Unpack
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Tuple_Unpack.Tuple_swap((10,20,30,40)),(10,20,30,40))

if __name__=="__main__":
    unittest.main()

