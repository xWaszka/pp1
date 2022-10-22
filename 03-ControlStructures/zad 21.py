#21.	The 'university' variable contains the name of university where you study. Write a program that displays the contents of the variable with an extra space between characters (add a space between each character).
university = "UEK w Krakowie"
for i in range (0, len(university)):
    print(university[i], end=" ")