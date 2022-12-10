f = open("numbers.txt", "r")
file = f.readlines()
sum = 0
for line in file:
    number = int(line)
    sum += number

print(f"sum = {sum}")
f.close()