import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Count_Upper_Lower
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Count_Upper_Lower.Uper_Lower("kesavJJHVah"),(4,7))

if __name__=="__main__":
    unittest.main()

