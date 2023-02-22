import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import max_min_dict
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(max_min_dict.max_dict({'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}),(600,100))

if __name__=="__main__":
    unittest.main()
