#wap to to factorial
#import unittest

#class Testadd(unittest.TestCase):
#    def test_add(self):
#        self.assertEqual(fact(8),40320)
  #  def test_case2(self):
  #      self.assertEqual(fact(5),120)


def fact(n):
    k=1
    for i in range(1,n+1):
        k = k * i
    return k
print(fact(8))

#if __name__=="__main__":
 #   unittest.main()
