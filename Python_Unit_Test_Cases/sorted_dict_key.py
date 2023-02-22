import sys
sys.path.append("D:/pyhon_test_programs")
import unittest
import sort_key
class testadd(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(sort_key.sort_d({'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}),{'Charlie': 12, 'Robert': 25, 'Tiffany': 22, 'Tim': 18})

if __name__=="__main__":
    unittest.main()

