#Python Program to Find the Number Occurring Odd Number of Times in a List
#import unittest
#class TestMap(unittest.TestCase):
#    def testcase1(self):
#        self.assertTrue(list(map(int,input("enter te list:").split())),{"3":2, "5":3, "7":2})
#    def testcase2(self):
#        self.assertTrue(list(map(int,input("enter te list:").split())),{"7":2, "9":3, "11":2})
def repeate(n):        
    k={}
    for i in n:
        if i%2 != 0 :
            c = n.count(i)
            k[i]=c
    #for i,v in k.items():
        #print(i,"repeates in",v)
    return k

#if __name__=="__main__":
 #   unittest.main()
