import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import add_nested_dict
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(add_nested_dict.nest_key({1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"}, 2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}),{1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat", "kesava":24}, 2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma", "modi":23}})

if __name__=="__main__":
    unittest.main()


