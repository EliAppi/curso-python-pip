#Metodo raiz cuadrada del profe
arr_objetivo=[4,5,100,81,7,11]
new_arr=[]

for objetivo in arr_objetivo:
    respuesta=0
    while respuesta**2<objetivo:
        #print(respuesta)
        respuesta+=1
        
    if respuesta**2==objetivo:
        #print(f"La raiz cuadrada de {objetivo} es {respuesta}")
        new_arr.append(objetivo)
    #else:
        #print(f"La raiz cuadrada de {objetivo} no es exacta")
        
print(new_arr)