#wap palindrome program
#import unittest
#class Tadd(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(palindrome(121),True)



def palindrome(n):
    if n == n[::-1]:
        return True
    else:
        return False

#if __name__ == "__main__":
#    unittest.main()
        
