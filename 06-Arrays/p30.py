def minimax(arr):
    maxi = max(arr)
    mini = min(arr)
    return mini, maxi

arr1 = [6,8,3,1,0,5,7]

print(minimax(arr1))