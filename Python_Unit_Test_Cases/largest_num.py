import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import largestNumInList
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(largestNumInList.list_add([4,5,6,9,12]),12)

if __name__=="__main__":
    unittest.main()

