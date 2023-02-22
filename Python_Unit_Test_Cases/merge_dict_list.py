import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import merge_dict
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(merge_dict.marge([1,2],[3,4]),{1: 2, 3: 4})

if __name__=="__main__":
    unittest.main()
