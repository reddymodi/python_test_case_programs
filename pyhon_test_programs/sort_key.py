#How can you sort dictionary elements based on keys d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
def sort_d(d):
    l = list(d.keys())
    l.sort()
    k = {}
    for j in l:
        for i,v in d.items():
            if  j == i:
                k[j] = v
            

    return k
d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}

print(sort_d(d))

