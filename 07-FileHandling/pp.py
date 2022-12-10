f = open("file.txt", "r", encoding="utf-8")
file = f.readlines()

for line in file:
    print(line,end="")

f.close()