nombre1=input("Ingresa tu nombre: ")
edad1=int(input("Que edad tienes?: "))
nombre2=input("Ingresa el nombre de tu compañero: ")
edad2=int(input("Que edad tiene?: "))

if edad1 > edad2:
    print(f"{nombre1} es mayor que {nombre2}")
elif edad1 < edad2:
    print(f"{nombre2} es mayor que {nombre1}")
else:
    print(f"{nombre1} y {nombre2} tienen la misma edad")