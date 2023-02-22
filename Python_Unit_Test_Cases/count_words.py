import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Count_Words_Chars
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Count_Words_Chars.Count_words("hii this kesava".split()),(3,13))

if __name__=="__main__":
    unittest.main()

