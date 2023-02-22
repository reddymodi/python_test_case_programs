import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import remove_nth_occur_index
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(remove_nth_occur_index.remove_nth_index(list(input("enter the list").split())),["my","name","is","kesav","is","modi"])

if __name__=="__main__":
    unittest.main()

