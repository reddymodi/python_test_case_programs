import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Count_vowels_set
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Count_vowels_set.Vowels("kesavarEdEU"),6)

if __name__=="__main__":
    unittest.main()

