#Python Program to Count Occurrences of Element in List
#import unittest
#class TestMap(unittest.TestCase):
#    def testcase1(self):
#       self.assertTrue(pr_repeat(list(map(int,input("enter ur list:").split()))))

def pr_repeat(n):
    k={}
    for i in n:
        c = n.count(i)
        k[i] = c 
    
    return k 

#3if __name__=="__main__":
 #   unittest.main()
