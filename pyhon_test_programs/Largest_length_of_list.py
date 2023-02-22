#Python Program to Return the Length of the Longest Word from the List of Words
#import unittest
#lass TestMap(unittest.TestCase):
 #   def testcase1(self):
  #      self.assertEqual(word_length(list(input("enter ur list:").split())),'kesava')
   #def testcase2(self):
    #    self.assertEqual(word_length(list(input("enter ur list:").split())),'modikesav')
def word_length(n):
    l = len(n[0])
    for i in range(1,len(n)):
        if l < len(n[i]):
            l = len(n[i])
    k=""
    for i in n:
        if len(i) == l:
            k += i 
   # print(k)
    return k

#if __name__=="__main__":
 #   unittest.main()
        
