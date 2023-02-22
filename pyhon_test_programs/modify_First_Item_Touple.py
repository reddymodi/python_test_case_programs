#Write a program to modify the first item (22) of a list inside a following tuple to 22 tuple1 = (11, [11, 33], 44, 55)
#import unittest
#class Testadd(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(modify((11, [11, 33], 44, 55)),(11, [11,22], 44, 55))
def modify(t):
    t[1][1] = 22
    print(t)
    return t

#if __name__=="__main__":
#    unittest.main()
