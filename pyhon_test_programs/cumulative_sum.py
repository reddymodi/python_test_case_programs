#Python Program to Find the Cumulative Sum of a List
#import unittest
#class testMap(unittest.TestCase):
 #   def testcase1(self):
  #      self.assertEqual(cumlative(list(map(int,input("enter ur list:").split()))),[1, 3, 6, 10, 15, 21])
def cumlative(n):
    k = []
    t = 0 
    for i in n:
        t += i 
        k .append(t)
    #print("cumlative sum is:",k)
    return k
print(cumlative([1,2,3,4,5]))
#if __name__=="__main__":
 #   unittest.main()
