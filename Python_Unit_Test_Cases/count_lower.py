import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Count_lower_in_String
class Testas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Count_lower_in_String.Lower_case("keSavaCa"),6)

if __name__=="__main__":
    unittest.main()
