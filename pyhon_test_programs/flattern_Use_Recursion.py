#import unittest
#class Testadd(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(flattern([1,[1,2],[1,2,3,4,[5]]]),[1, 1, 2, 1, 2, 3, 4, 5])
#def testcase2(self):
#        self.assertEqual(flattern([1,[1,2],[1,6,5,9,[5]]]),[1, 1, 2, 1, 6, 5, 9, 5])
def flattern(n):
    if n == []:
        return n
    if isinstance(n[0],list):
        return flattern(n[0]) + flattern(n[1:])
    return n[:1] + flattern(n[1:])

#if __name__=="__main__":
    unittest.main()
