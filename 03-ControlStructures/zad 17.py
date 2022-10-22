#17. Let x and y denote the coordinates of a point on the plane. Write a program that determines in which quadrant of the coordinate system the point P (x, y) is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system.
x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

if x > 0 and y > 0:
    print("I")
elif x > 0 and y < 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x < 0 and y > 0:
    print("IV")    