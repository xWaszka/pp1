def compare(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(0,len(arr1)):
        if arr1[i] == arr2[i]:
            continue
        else:
            return False
    return True

a1 = ["water", "book", "sky"]
a2 = ["water", "book", "sky"]
b1 = [True,False]
b2 = [True,False,True]
c1 = [5,3,1]
c2 = [5,3,1]
d1 = [3,2,1]
d2 = [3,2]

print(compare(d1,d2))