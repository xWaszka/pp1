person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person["name"])
print(person["hobby"])
person["surname"] = "Nowak"
person["married"] = False
person["gender"] = "male"
person["hobby"] += ["bicycle"]
person["phone"]["work"] = "313131444"
print(person)
