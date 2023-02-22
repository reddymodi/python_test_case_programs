#import unittest
#class Testcase(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(twossum([2,4,3],[5,6,4]),708)
def twossum(l1,l2):
    k = ""
    v = ""
    for i in l1:
        k += str(i)
    for j in l2:
        v += str(j)
    y = str(int(k) + int(v))
 #   print(y[::-1])
    return int(y[::-1])


#if __name__=="__main__":
#    unittest.main()
