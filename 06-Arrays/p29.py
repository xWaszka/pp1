arr1 = [6,8,3,1,0,5,7,22,66,33,11,23,546,123231]

x = int(input("Podaj liczbę: "))

count = 0

for i in arr1:
    if x < i:
        count+=1
        
print("Liczba elementów większych od twojej liczby to: " + str(count))