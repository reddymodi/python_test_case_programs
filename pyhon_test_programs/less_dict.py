#filter dictionary where the value is less than 20000.
	#empdict = {'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}
def dict_ct(d):
    k={}
    for i,v in d.items():
        if v < 20000:
            k[i]=v
    return k
d={'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}
print(dict_ct(d))
