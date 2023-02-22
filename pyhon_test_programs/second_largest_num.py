#wap second largest program#
#import unittest
#class Testadd(unittest.TestCase):
#    def testcase(self):
#        self.AssertEqual(second_large(list(map(int,input("enter ur list:").split()))),24)
        
def second_large(n):
    n.sort()
    return n[len(n)-2]

#if __name__=="__main__":
#    unittest.main()
