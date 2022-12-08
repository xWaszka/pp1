def occurs(number, array):
    if number in array:
        return print("Number " + str(number) + " appears in the array")
    else:
        return print("Number " + str(number) + " does not appear in the array")

arr = [15, 38, 7, 23, 14]

occurs(23,arr)
    