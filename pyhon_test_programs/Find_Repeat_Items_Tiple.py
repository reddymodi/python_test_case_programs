#Write a Python program to find the repeated items of a tuple
#import unittest
#class testad(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(find_rep(tuple(input("enter ur tuple:").split())),['2','3','4','5','6'])
def find_rep(t):
    c = []
    for i in t:
        h=t.count(i)
        if h != 1:
            if i not in c:
                c.append(i)
                
    #print(*c)
    return c

#if __name__=="__main__":
 #   unittest.main()
