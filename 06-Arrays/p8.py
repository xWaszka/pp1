arr = [-15,8,-31,47,-2,19]
max = 0
min = 99
for i in range(0,len(arr)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

print(max,min)