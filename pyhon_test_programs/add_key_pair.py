#Python Program to Add a Key-Value Pair to the Dictionary
def dict_key(d):
    d["e"]=42
    return d
d = {"a":12, "b":23, "c":45}
print(dict_key(d))
