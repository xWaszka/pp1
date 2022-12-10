file = open("countries.txt", "r")
file_content = file.readlines()
l = 1
for line in file_content:
    print(l, line,end="")
    l+=1

file.close()