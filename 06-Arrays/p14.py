arr = [[True,False],[True,True],[False,False]]

for i in range (0, len(arr)):
    for j in range(0, len(arr[0])):
        arr[i][j] = not arr[i][j]

print(arr)