#import unittest
#class Testadd(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(pr_even([2,5,8,9,6]),8)
#
#    def testcase2(self):
#        self.assertEqual(pr_odd([2,5,8,9,6]),9)
        


def pr_even(n):
    #n=list(map(int,input("enter ur list").split()))
    Ev = []
    Od = []
    for i in n:
        if i%2==0:
            Ev.append(i)
        else:
            Od.append(i)
    Ev.sort()
    Od.sort()
    ev_L=Ev[len(Ev)-1]
    od_l=Od[len(Od)-1]
    return (ev_L,od_l)


#def pr_odd(n):
 #   Od=[]
 #   for i in n:
 #       if i%2 != 0:
 #           Od.append(i)
 #   Od.sort()
 #   return (Od[len(Od)-1])

#if __name__=="__main__":
 #   unittest.main()
