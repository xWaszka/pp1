arr1 = [2,3,2,5,8,1,9,8]
arr2 = []

for i in arr1:
    if i not in arr2:
        arr2.append(i)
        
print(arr2)