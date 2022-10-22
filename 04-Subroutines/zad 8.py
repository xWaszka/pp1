#8.	Define a function that displays integer numbers from 1 to N. Then call the function and display numbers from 1 to 15.

def funkcja(x):
    for i in range(1, x+1):
        print(i, end=" ")
    print()
    
funkcja(15)
funkcja(12)