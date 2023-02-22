#Python Program to Count the Number of Words and Characters in a String
#import unittest
#class Testadd(unittest.TestCase):
#    def testcase(self):
 #       self.assertEqual(Count_words_chars((input("enter ur string: ").split())),(4,13))
def Count_words(s):
    ch = 0
    w = 0
    if len(s) == 0:
        print("enter a valid string")
    else:
        for i in s:
            w += 1
            for j in i:
                ch += 1 
    #print("words: ",w)
    #print("characters: ",ch)
    return (w,ch)
print(Count_words("hii this kesav".split()))
#if __name__=="__main__":
 #   unittest.main()
