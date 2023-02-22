#Write a Python program to convert a tuple to a dictionary t = (("Name", "Ram"),("Age", 23),("City", "Bangalore"),("Marks", 422))
import unittest
class Testmap(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(dict_tup((("Name", "Ram"),("Age", 23),("City", "Bangalore"),("Marks", 422))),{"Name":"Ram", "Age":23, "City":"Bangalore", "Marks":422})
def dict_tup(t):
    k={}
    for i in t:
        k[i[0]]=i[1]
    print(k)
    return k

if __name__=="__main__":
    unittest.main()
