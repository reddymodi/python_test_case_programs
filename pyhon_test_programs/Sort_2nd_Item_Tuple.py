#Sort a tuple of tuples by 2nd itemtuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
#import unittest
#class Testadd(unittest.TestCase):
 #   def testcase1(self):
 #       self.assertEqual(second_tuple((('a', 23),('b', 37),('c', 11), ('d',29))),(('c',11),('a',23),('d',29),('b',37)))
def second_tuple(t):

    l=[]
    for i in range(len(t)):
        l.append(t[i][1])
    l.sort()
    m=[]
    for i in range(len(l)):
        for j in t:
            if l[i] == j[1]:
                if j not in m:
                    m.append(j)
  #  print(tuple(m))
    return tuple(m)

#if __name__=="__main__":
#    unittest.main()
