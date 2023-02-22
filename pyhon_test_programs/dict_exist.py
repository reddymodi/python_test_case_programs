#Python Program to Check if a Key Exists in a Dictionary or Not
def dict_ex(d,k):
    for i,v in d.items():
        if i == k:
            return True
        else:
            return False
d = {"a":12, "b":23, "c":45}
k = input("enter ur key: ")
print(dict_ex(d,k))

