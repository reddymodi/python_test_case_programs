import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import modify_First_Item_Touple
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(modify_First_Item_Touple.modify((11, [11, 33], 44, 55)),(11, [11,22], 44, 55))

if __name__=="__main__":
    unittest.main()
