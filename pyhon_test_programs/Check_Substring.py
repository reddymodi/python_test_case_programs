#Python Program to Check if the Substring is Present in the Given String
#import unittest
#class Testadd(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(Check_sub(input("enter ur string: "),input("enter ur string: ")),True)
def Check_sub(s1,s2):
    if s2 in s1:
        return True
    else:
        return False
print(Check_sub("kesavmodi","modi"))

#if __name__=="__main__":
#    unittest.main()
