#wap to  create a tuple first element is number and second element is square of the number
#import unittest
#class Testadd(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(square_num(5),((1,1), (2,4), (3,9), (4,16), (5,25)))
def square_num(n):
    k=[]
    for i in range(1,n+1):
        l=i**2
        k.append((i,l))
    #print(tuple(k))
    return tuple(k)
 
#if __name__=="__main__":
#    unittest.main()
