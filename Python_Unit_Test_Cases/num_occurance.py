import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Num_of_Occurance
class Testas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Num_of_Occurance.Occur((50, 10, 60, 70, 10)),2)

if __name__=="__main__":
    unittest.main()
