arr1 = [4,36,12,28,9,44,5]
arr2 = [15, 8, 31, 47, 2, 19]
arr3 = [22,54,12,1,52,24]

def bubblesort(arr):
    for i in range(0,len(arr)-1):
        s = 0
        if arr[i] > arr[i+1]:
            s = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = s
            bubblesort(arr)
            
    return arr

print(bubblesort(arr3))