#remove no value items from Dictionary
	#mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
def remvl(d):
    for i,v in d.items():
        if d[i]==None:
            del d[i]
    return d
d={'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
print(remvl(d))
