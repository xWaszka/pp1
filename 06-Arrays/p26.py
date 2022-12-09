arr = [5,1,9,6,1]
max = max(arr)
max1 = arr[0]
for i in arr:
    if i > max1 and i < max:
        max1 = i
print(max1)