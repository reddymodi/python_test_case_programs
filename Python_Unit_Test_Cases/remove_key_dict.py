import sys
sys.path.append("D:\pyhon_test_programs")
import unittest
import remove_dict
class Testase(unittest.TestCase):
    def testcase(self):
        self.assertEqual(remove_dict.key_re({"a":12, "b":23, "c":45},"b"),{"a":12, "c":45})

if __name__=="__main__":
    unittest.main()


