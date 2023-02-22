#import unittest
#class Testadd(unittest.TestCase):
#    def testcase(self):
#        self.assertEqual(common_char(input("enter first string: "),input("enter first string: ")),"kesv")
def common_char(s1,s2):
    k = ""
    if len(s1) == 0:
        print("enter a valid string")
    else:
        for i in s1:
            for j in s2:
                if i == j:
                    if i not in k:
                        k += i 
 #   print("common string is:",k)
    return k
#if __name__=="__main__":
 #   unittest.main()
