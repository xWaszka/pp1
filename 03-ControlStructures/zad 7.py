#7.	X contains any integer value. Write a program to check that the value is even.
x = int(input("Podaj X: "))
if x % 2 == 0 and x > 0:
    print("parzysta")
elif x == 0:
    print("liczba to zero")
else:
    print("nieparzysta")