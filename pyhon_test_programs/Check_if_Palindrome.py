#Python Program to Check if a Given String is Palindrome 
#import unittest
#class Testadd(unittest.TestCase):
 #   def testcase1(self):
  #      self.assertEqual(palindrome(input("enter ur string: ")),True)
def palindrome(s):

    if s == s[::-1]:
        return True
    else:
        return False
print(palindrome("121"))
#if __name__=="__main__":
 #   unittest.main()
        
