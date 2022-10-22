#20.Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user. Sample result:
a = int(input("Podaj liczbę do przemnożenia: "))
for i in range(1, 11):
    # print(a, "x", i,"=",a*i)
    print(f"{a} x {i} = {a*i}")
    