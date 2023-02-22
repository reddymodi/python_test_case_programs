#Python Program to copy from one dictionary to another
def cp(d):
    c=d.copy()
    return c
d={"a":3, "b":4, "c":5}
print(cp(d))
