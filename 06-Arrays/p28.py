def bubblesort(arr):
    for i in range(0,len(arr)-1):
        s = 0
        if arr[i] > arr[i+1]:
            s = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = s
            bubblesort(arr)
            
    return arr

arr1 = [1,0,9,4,6]
arr2 = [6,8,3,1,0,5,7]

median1 = 0
median2 = 0

if len(arr1)+1 % 2 != 0:
    len1 = len(arr1) // 2
    len2 =  len(arr1) // 2 + 1
    arr1 = bubblesort(arr1)
    median1 = int((arr1[len1]+arr1[len2]) / 2)
else:
    arr1 = bubblesort(arr1)
    median1 = int(arr1[len(arr1)/2])

print(median1)

if len(arr2)+1 % 2 != 0:
    len1 = len(arr2) // 2
    len2 =  len(arr2) // 2 + 1
    arr2 = bubblesort(arr2)
    median2 = int((arr2[len1]+arr2[len2]) / 2)
else:
    arr2 = bubblesort(arr2)
    median2 = int(arr2[len(arr2)/2])

print(median2)