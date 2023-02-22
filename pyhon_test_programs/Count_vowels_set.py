#Python Program to Count the Number of Vowels in a String
#import unittest
#class testadd(unittest.TestCase):
 #   def testcase(self):

 #       self.assertEqual(Vowels(input("enter ur characters: ")),4)
def Vowels(s):
    vowels = "aeiouAEIOU"
    c = 0
    for i in s:
        for j in vowels:
            if i == j:
                c += 1
    #print("vowels ocunt is: ",c)
    return c
print(Vowels("kesavareddy"))
#if __name__=="__main__":
 #   unittest.main()
