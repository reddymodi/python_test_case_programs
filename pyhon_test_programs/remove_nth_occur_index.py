#Python Program to Remove the ith Occurrence of the Given Word in a List
#import unittest
#class Testmap(unittest.TestCase):
#    def testcase1(self):
#        self.assertEqual(remove_nth_index(list(input("enter the list").split())),["my","name","is","kesav","is","modi"])
def remove_nth_index(n):
    k = input("enter the word:")
    m = int(input("enter the occurance"))
    c =[]
    count =0 
    for i in n:
        if i == k:
            count += 1
            if count != m:
                c.append(i)
         
        else:
            c.append(i)     
    if count == 0:
        return ("item not found")
    else:
        return c
#if __name__=="__main__":
#    unittest.main()
