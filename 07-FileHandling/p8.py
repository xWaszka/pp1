f = open("eula.3082.txt", "r")
file = f.readlines()

for line in file:
    print(line,end="")

f.close()