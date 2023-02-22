#Python Program to Swap the First and Last Element in a List
#import unittest
#class Testmap(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(swap_list(list(map(int,input("enter ur list:").split()))),[6,3,2,1,4])
def swap_list(n):        
    l = len(n)
    y = n[l-1]
    i = n[0]
    n[0]=y
    n[l-1]=i
 #   print(n)
    return n

#if __name__=="__main__":
#    unittest.main()
