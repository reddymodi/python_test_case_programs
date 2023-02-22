#Counts the number of occurrences of item 10 from a tuple1 = (50, 10, 60, 70, 10)
#import unittest
#class TestMap(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(Occur(tuple(input("enter ur tuple:").split())),2)
def Occur(t):
    c = 0
    for i in t:
        i = int(i)
        if i == 10:
            c += 1
 #   print(c)
    return c

#if __name__=="__main__":
#    unittest.main()
