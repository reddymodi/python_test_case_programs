#Access value 20 from the tuple  tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
#import unittest
#class Testad(unittest.TestCase):
    #def testcase1(self):
        #self.assertEqual(tuple_ch(("Orange", [10, 20, 30], (5, 15, 25))),20)
def tuple_ch(t):

    k = t[1][1]
    print(k)
    return k

#if __name__=="__main__":
#  unittest.main()
