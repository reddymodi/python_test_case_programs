#How to get min and max keys corresponding to min and max value in Dictionary
     #fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
def max_dict(d):
    k=[]
    for i,v in d.items():
        v = int(v)
        k.append(v)
    m=max(k)
    n=min(k)
    return (m,n)
d={'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
print(max_dict(d))
