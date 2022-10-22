#6.	The speed limit on the motorway is 130 km / h. Write a program that checks whether a car exceeded the speed limit.
speed = int(input("Predkosc pojazdu: "))
if speed > 130:
    print("Limit predkosci przekroczony")
else:
    print("Ponizej limitu predkosci")