import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import delete_dict
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(delete_dict.deleted({1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}),{1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},2: {'name': 'rohit', 'age': '37', "lastname":"sharma"}})

if __name__=="__main__":
    unittest.main()

