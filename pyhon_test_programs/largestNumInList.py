#wap largest num
#import unittest
#class Testcadd(unittest.TestCase):
#    def testcase(self):
#        self.assertEqual(list_add([4,5,6,9,12]),12)




def list_add(n):
    k=sorted(n)
    return k[len(k)-1]



#if __name__=="__main__":
 #   unittest.main()
