import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import sort_value
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(sort_value.sort_key({'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}),{'Charlie': 12, 'Tim': 18, 'Tiffany': 22, 'Robert': 25})

if __name__=="__main__":
    unittest.main()

