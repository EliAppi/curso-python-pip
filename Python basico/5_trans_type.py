name="Eli"
print(type(name))
name=47
print(type(name))
name=True
print(type(name))

print("Eli"+"Piñeros")
print(23+15)
print("Eli"+str(58)) #error type

age=31
print("Mi edad es "+str(age))
print(f"Mi edad es {age}") #Con format se cambia el tipo automaticamente

age=input("Cual es tu edad? ")
print(type(age))
age=int(age)+10
print(f"Tu edad en 10 años sera {age} años")