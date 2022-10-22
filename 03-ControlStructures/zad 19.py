#19. Write a program that calculates a dog's age in dog’s years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years.
HDogAge = int(input("Podaj wiek psa w ludzkich latach: "))
DogAge = 0
for i in range(1, HDogAge + 1):
    if i < 3:
        DogAge += 10.5
    else:
        DogAge +=4
    
print("Wiek psa w psich latach:", DogAge)