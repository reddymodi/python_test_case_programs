#Unpack the tuple into 4 variables tuple1 = (10, 20, 30, 40)
#import unittest
#class Testmap(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(Tuple_swap((10, 20, 30, 40)),(10,20,30,40))
def Tuple_swap(t):
    t = (10, 20, 30, 40)
    t1,t2,t3,t4=t
    #print(t1)
    #print(t2)
    #print(t3)
    #print(t4)
    return (t1,t2,t3,t4)

if __name__=="__main__":
    unittest.main()
