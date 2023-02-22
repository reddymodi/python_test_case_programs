#wap to print armstrong num
#import unittest

#class Testadd(unittest.TestCase):
 #   def testcase1(self):
 #       self.assertTrue(arm(153))

def arm(n):
    k=0
    n=str(153)
    for i in n:
        i = int(i)
        k += i ** len(n)
    if k == int(n):
        return True
    else:
        return False
print(arm(153))
#if __name__=="__main__":
#    unittest.main()

