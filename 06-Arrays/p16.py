arr = [15, 8, 31, 47, 2, 19]

for i in arr:
    print(i, end=" ")
    
print("")
for i in range(1, len(arr)+1):
    print(arr[-i], end=" ")