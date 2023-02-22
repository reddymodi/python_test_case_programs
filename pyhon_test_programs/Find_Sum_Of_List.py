#Python Program to Find the Sum of Elements in a List using Recursion
#import unittest
#class Testmap(unittest.TestCase):
 #   def testcase1(self):
  #      self.assertEqual(list_sum(list(map(int,input("enter ur list:").split()))),24)

   # def testcase2(self):
    #    self.assertEqual(list_sum(list(map(int,input("enter ur list:").split()))),42)
        
def list_sum(n):
    l=len(n)
    su = 0
    if l ==0:
        return 0
    else:
        for i in n:
            su += i

    #print(su)
    return su

        
        
#if __name__=="__main__":
 #   unittest.main()
