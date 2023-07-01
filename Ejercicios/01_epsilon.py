#Busqueda de reices con aproximacion de soluciones
objetivo = int(input('Escoge un numero: '))
epsilon = 0.01    #Que tan preciso. Entre mas preciso mas tiempo demora
paso = epsilon**2   #0.0001*0.0001
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:  #abs= valor absoluto
    #print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')