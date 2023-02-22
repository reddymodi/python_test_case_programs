#Python Program to Find the Sum of All the Items in a Dictionary
def sum_d(d):
    s = 0
    for i,v in d.items():
        s += int(v)
    return s
        
d={"a":12, "b":23, "c":45}
print(sum_d(d))
