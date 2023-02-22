import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import remove_none
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(remove_none.remv({'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}),{'lang': 'C#', 'Fruit': 'Apple'})

if __name__=="__main__":
    unittest.main()

