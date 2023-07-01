#Método de la bisección funciona solo con conjuntos ordenados
#Cortar espacios de busqueda para que sea mas eficiente
objetivo = int(input('Escoge un numero: '))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0, objetivo)   #max(valor1,valor2) regresa valor mas alto entre dos valores
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta

    respuesta = (alto + bajo) / 2 #Busqueda binaria= Cada interaccion estamos dividiendo el espacio de busqueda en dos

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
