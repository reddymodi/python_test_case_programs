def freq(d):
    k={}
    for i in d:
        c=d.count(i)
        k[i]=c
    return k
d="my name is kesava reddy modi kesava".split()
print(freq(d))
