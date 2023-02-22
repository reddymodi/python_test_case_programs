import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import remove_dup_in_list
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(remove_dup_in_list.remove_dup(list(map(int,input("enter ur list:").split()))),[4,5,3,7,9])

if __name__=="__main__":
    unittest.main()
