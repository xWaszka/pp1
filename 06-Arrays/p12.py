from ctypes import sizeof


arr = [[2,5,4],[9,0,3]]

print(arr)
print(len(arr),len(arr[0]))
print(arr[0][1])
print(arr[1][2])
print(arr[1][0],arr[1][1],arr[1][2])
for i in range(0,len(arr)):
    for j in range(0,len(arr[0])):
        print(arr[i][j], end=" ")
    print("")