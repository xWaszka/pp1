import math
height = int(input("Wprowadź swój wzrost: "))
weight = int(input("Wprowadź swóją wagę: "))
bmi = weight/height**2*10000000 // 10
bmi = bmi/100
print("Twoje BMI:", bmi)