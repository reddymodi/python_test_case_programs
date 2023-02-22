#Python Program to Count Number of Lowercase Characters in a String
#import unittest
#class TestAdd(unittest.TestCase):
#    def testcase(self):
#        self.assertEqual(Lower_case(input("enter ur string: ")),4)
def Lower_case(s):
    c = 0
    for i in s:
        d=int(ord(i))
        if (97 <= d <= 122):
            c += 1
    return c
print(Lower_case("kEsavEv"))
#if __name__=="__main__":
 #   unittest.main()
