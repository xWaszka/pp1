from cmath import sqrt


a = int(input("Wprowadz a: "))
b = int(input("Wprowadz b: "))
c = int(input("Wprowadz c: "))
s = (a+b+c)/2
pole = sqrt(s*(s-a)*(s-b)*(s-c))
print(pole)