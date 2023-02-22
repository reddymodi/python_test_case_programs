#Python Program to Determine How Many Times a Given Letter Occurs in a String
#import unittest

#class Testad(unittest.TestCase):
#    def testcase(self):
 #       self.assertEqual(occur(input("enter ur string: "),input("enter ur letter: ")),3)
def occur(s,l):
    c = 0
    for i in s:
        if i == l:
            c += 1
    #print(l,"is",c,"times")
    return c
print(occur("kesava","a"))
if __name__=="__main__":
    unittest.main()
