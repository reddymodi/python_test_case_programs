#Python Program to Find Average of a List
#import unittest
#class Testmap(unittest.TestCase):
#    def testcas1(self):
#        self.assertEqual(pr_avarage(list(map(int,input("enter ur list").split()))),3.5)
#   def testcas2(self):
#        self.assertEqual(pr_avarage(list(map(int,input("enter ur list").split()))),4)
#    def testcas3(self):
#        self.assertEqual(pr_avarage(list(map(int,input("enter ur list").split()))),4.5)
def pr_avarage(n):
    l = int(len(n))
    total = 0
    for i in n:
        total += i
    avg = total/l
    #print("avarage:",avg)
    return avg

#if __name__=="__main__":
 #   unittest.main() 
