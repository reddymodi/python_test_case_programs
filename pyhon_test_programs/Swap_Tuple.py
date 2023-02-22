#Swap two tuples in Python  tuple1 = (1,2),tuple2 = (3,4)
#import unittest
#class Testmap(unittest.TestCase):
    #    def testcase1(self):
 #      self.assertEqual(swwap((1,2),(3,4)),(3,4),(1,2))
def swwap(t1,t2):
    k = t1
    t1 = t2
    t2 = k
   #print(t1)
    #print(t2)
    return (t1,t2)

#if __name__=="__main__":
#    unittest.main()
