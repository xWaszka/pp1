from multiprocessing.dummy import Array


array = [2,3,7,5,4]
def f(array):
    print(array) #a
    print(len(array)) #b
    print(array[0]) #c
    print(array[1]) #d
    print(array[-1]) #e
    print(array[-2]) #f
    print(array[0]+array[-1]) #g
    print(array[int(len(array)/2)]) #h
    for i in array: #i
        print(i, end=" ")
    print("")
    for i in range(0,int(len(array)//2)+1): #j
        print(array[i], end=" ")
    
    return ""
print(f(array))