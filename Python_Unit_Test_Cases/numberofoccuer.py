import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import print_repeated_word
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(print_repeated_word.pr_repeat(list((input().split()))),{"hi":1, "this":2, "is":1, "modi":2})

if __name__=="__main__":
    unittest.main()
