#16.	Write a program that displays two numbers entered from the keyboard in ascending order.
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
if a >= b:
    print(a,b)
else:
    print(b,a)