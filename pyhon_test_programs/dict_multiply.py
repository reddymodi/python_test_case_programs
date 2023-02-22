#Python Program to Multiply All the Items in a Dictionary
def multiply(d):
    m=1
    for i,v in d.items():
        m *= int(v)
    return m
d={"a":12, "b":23, "c":45}
print(multiply(d))
