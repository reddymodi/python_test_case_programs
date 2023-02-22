def less_d(d):
    k=list(d.values())
    k.sort()
    l = len(k)-1

    m={}
    while l >= 0:
        for i,v in d.items():
            if v == k[l]:
                m[i]=k[l]
                l -= 1
    return m
d={"A":3, "b":1, "c":2,"d":5, "l":4, "m":9}
print(less_d(d))
