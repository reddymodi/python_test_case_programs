import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import less_dict
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(less_dict.dict_ct({'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}),{'Jack':12000})

if __name__=="__main__":
    unittest.main()
