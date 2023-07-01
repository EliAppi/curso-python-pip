def enumeracion(objetivo):
    respuesta=0

    while respuesta**2<objetivo:
        #print(respuesta)
        respuesta+=1
        
    if respuesta**2==objetivo:
        print(f"La raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f"{objetivo} no tiene raiz cuadrada excacta")
        
def aproximacion(objetivo):
    #Busqueda de reices con aproximacion de soluciones
    
    epsilon = 0.01    #Que tan preciso. Entre mas preciso mas tiempo demora
    paso = epsilon**2   #0.01*0.01
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:  #abs= valor absoluto
        #print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')
        
def biseccion(objetivo):
    #Método de la bisección funciona solo con conjuntos ordenados
    #Cortar espacios de busqueda para que sea mas eficiente
    epsilon = 0.0000001
    bajo = 0.0
    alto = max(1.0, objetivo)   #max(valor1,valor2) regresa valor mas alto entre dos valores
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        #print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2 #Busqueda binaria= Cada interaccion estamos dividiendo el espacio de busqueda en dos

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def run():
    '''Descripcion de lo que hace la funcion'''
    opcion_repeticion=int(input("Cuantas veces deseas probar los metodos: "))
    i=0
    objetivo = int(input('Escoge un numero: '))
    
    while(i<opcion_repeticion):
        print("*"*10)  #Imprime separador manual de operaciones
        print("Elige el metodo para resolver la raiz")
        opcion_metodo=input("Metodos: enumeracion, aproximacion o biseccion: ").lower()
        

        if opcion_metodo=="enumeracion":
            enumeracion(objetivo)
        elif opcion_metodo=="aproximacion":
            aproximacion(objetivo)
        elif opcion_metodo=="biseccion":
            biseccion(objetivo)
        else:
            print("*"*10)  #Imprime separador manual de operaciones
            print("ATENCION: Metodo mal escrito, intenta nuevamente")
            i-=1 #Resto para nuevo intento
        i+=1

run()