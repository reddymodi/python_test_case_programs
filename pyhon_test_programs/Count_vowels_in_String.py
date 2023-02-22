#Python Program to Count Number of Vowels in a String using Sets
#import unittest
#class Testadd(unittest.TestCase):
#   def testcase(self):
 #       self.assertEqual(vowel(set(input("enter ur string:"))),5)
def vowel(s):
    vowels="aeiouAEIOU"
    c = 0
    for i in vowels:
        if i in s:
            c += 1
    #print(c)
    return c
print(vowel("kesavae"))
#if __name__=="__main__":
 #   unittest.main()
