import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Nested_Sorted_second_list
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Nested_Sorted_second_list.Nest_sort((("a", 3, 5), ('b', 5, 7), ("c", 2, 6), ("d", 9), ("e",2,3))),(("c",2,6),("e",2,3),("a",3,5),("b",5,7),("d",9)))

if __name__=="__main__":
    unittest.main()
