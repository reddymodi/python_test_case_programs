#Python Program to Find the Total Sum of a Nested List Using Recursion
#import unittest
#lass Testmap(unittest.TestCase):
#  def testcase1(self):
#        self.assertEqual(find_total([1,[1,2],[3,4,5]]),16)
#    def testcase2(self):
#        self.assertEqual(find_total([10,[8,2],[3,9,5]]),37)
def find_total(n):
    k=[]
    for i in n:
        if type(i) == list:
            for j in i:
                k.append(j)
        else:
            k.append(i)
    total = sum(k)
    #print(total)
    return total


#if __name__=="__main__":
 #   unittest.main()
