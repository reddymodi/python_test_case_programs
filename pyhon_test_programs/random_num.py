import unittest,random

class testMap(unittest.TestCase):
    def testcase1(self):
       self.assertTrue(random(int(input("enter the range:"))))
    def testcase2(self):
       self.assertTrue(random(int(input("enter the range:"))))

def random(m):
    n = []
    for i in range(m):
        n.append(random.randint(1,20))
    print(n)

if __name__=="__main__":
    unittest.main()
