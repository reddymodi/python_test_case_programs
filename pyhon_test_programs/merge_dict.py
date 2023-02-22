#Python Program to Map Two Lists into a Dictionary
def marge(l1,l2):
    d={}
    d[l1[0]]=l1[1]
    d[l2[0]]=l2[1]
    return d

l1=[1,2]
l2=[3,4]

print(marge(l1,l2))

