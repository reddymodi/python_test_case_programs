#Python Program to Find the Larger String without using Built-in Functions
#import unittest
#class testad(unittest.TestCase):
#   def testcase(self):
 #       self.assertEqual(Find_large((input("enter ur string: ").split())),'kesava')
def Find_large(s):
    l = len(s)
    k = int(len(s[0]))
    for i in range(l):
        if int(len(s[i])) > k:
            k = int(len(s[i]))
    for i in range(l):
        if int(len(s[i])) == k:
            #print(s[i])
            return s[i]

    
#if __name__=="__main__":
#    unittest.main()
