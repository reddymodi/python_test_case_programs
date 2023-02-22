import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Largest_length_of_list
class Testas(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Largest_length_of_list.word_length(list(input("enter ur list:").split())),'modikesav')


if __name__=="__main__":
    unittest.main()
