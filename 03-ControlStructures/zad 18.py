#18.There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.
money = int(input("Podaj liczbę ZŁ: "))
p = 0
d = 0
j = 0

p = money // 5
money = money % 5
d = money // 2
money = money % 2
j = money
print("Piątki:", p)
print("Dwójki:", d)
print("Jedynki:", j)

