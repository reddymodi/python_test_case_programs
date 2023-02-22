import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import frequancy_dict
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(frequancy_dict.freq("my name is kesava reddy modi kesava".split()),{'my': 1, 'name': 1, 'is': 1, 'kesava': 2, 'reddy': 1, 'modi': 1})

if __name__=="__main__":
    unittest.main()
