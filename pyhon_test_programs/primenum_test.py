#wap to primenumber
#import unittest

#class Testadd(unittest.TestCase):
#    def testcase1(self):
#        self.assertTrue(prime_num(5))


def prime_num(n):
    c = False
    if n == 1:
        c = False
    else:
        for i in range(2,n+1):
            if n%i == 0:
                c = False
        else:
            c = True
    return c


#if __name__=="__main__":
#    unittest.main()
