arr = ["Film1", "Film2", "Film3", "Film4", "Film5"]
f = open("films.txt", "w")

for i in arr:
    f.write(i + "\n")
f.close()