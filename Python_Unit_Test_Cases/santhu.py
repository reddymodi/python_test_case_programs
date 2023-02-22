n=[12,10,3,6,10,15,18]
n1 = [-3,6,2,-5,3]
l=2
res=[]


for i in n1:
    if i < l:
        res.append(i)
    for j in res:
        if j < l:
            res.append(i)
        
#print(m)
#print(z)
#print(y)
print(res)
