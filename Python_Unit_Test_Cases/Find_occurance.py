import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import Find_occurances_char
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(Find_occurances_char.occur("kesava","a"),2)

if __name__=="__main__":
    unittest.main()

