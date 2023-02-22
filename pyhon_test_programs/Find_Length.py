#import unittest
#class Testad(unittest.TestCase):
 #   def testcase(self):
  #      self.assertEqual(length(input("enter ur string: ")),6)
def length(s):
    c = 0
    for i in s:
        c += 1 
    #print("lengt is: ",c)
    return c
print(length("kesava"))
#if __name__=="__main__":
 #   unittest.main()
