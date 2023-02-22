#write a program sort a nested tuple in second item
#import unittest
#class testmap(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(Nest_sort((("a", 3, 5), ('b', 5, 7), ("c", 2, 6), ("d", 9), ("e",2,3))),(("c",2,6),("e",2,3),("a",3,5),("b",5,7),("d",9)))
def Nest_sort(t):
    l=[] #its empty list
    for i in t:
        l.append(i[1]) #add the item in to list
    l.sort()   #its sort the l list
    y=[]  #its empty list
    for j in l:
        for i in t:
            if j == i[1]: #it l list items and t tuple itms are equal then condition is true 
                if i not in y:
                    y.append(i) # append the items in to y list
#    print("sorted tuple is",tuple(y))
    return tuple(y)

#if __name__=="__main__":
#    unittest.main()
