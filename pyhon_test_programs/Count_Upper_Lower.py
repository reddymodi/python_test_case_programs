#Python Program to Count Number of Uppercase and Lowercase Letters in a String
#import unittest
#class Testadd(unittest.TestCase):
#    def testcase(self):
#        self.assertEqual(Uper_Lower(input("enter ur string: ")),(4,5))
def Uper_Lower(s):
    u = 0
    l = 0
    for i in s:
        if i == i.lower():
            l += 1
        else:
            u += 1
            
    #print("uppercase letters is: ",u)
    #print("lowercase lettrs is: ",l)
    return (u,l)
print(Uper_Lower("kesavaJjk"))
#if __name__=="__main__":
#    unittest.main()
