f = open("shopping.txt", "a")
while True:
    product = input("enter a product: ")
    if product == "":
        break
    f.write(product+ "\n")

f.close()