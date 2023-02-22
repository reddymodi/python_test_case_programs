import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Find_Length
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Find_Length.length("kesava"),6)

if __name__=="__main__":
    unittest.main()

