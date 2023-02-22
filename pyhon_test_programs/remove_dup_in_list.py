#Python Program to Remove Duplicates from a List
#import unittest
#class TestMap(unittest.TestCase):
#    def testcase1(self):
#       self.assertEqual(remove_dup(list(map(int,input("enter ur list:").split()))),[4,5,3,7,9])
#    def testcase2(self):
#       self.assertEqual(remove_dup(list(map(int,input("enter ur list:").split()))),[4,5,3,2,1])
def remove_dup(n):
    k = []
    for i in n:
        if i not in k:
            k.append(i)
 #   print("uniqe list:",k)
    return k
            
#if __name__=="__main__":
#    unittest.main()
