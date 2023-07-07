''' Enunciado: Encontrar cuántos cuadrados hay en un conjunto de puntos. Recuerde que un cuadrado tiene todos sus lados iguales.
    Argumentos: Array de String
    Condiciones de la entrada:  Todos los puntos dados por (x, y) son coordenadas enteras con números no negativos menores o iguales a 1000. No habrá dos puntos repetidos en la entrada. 
                                Todos los cuadrados que se deben contar son los que tienen dos lados paralelos a cada uno de los ejes. 
                                Dos triángulos son considerados iguales si los cuatro puntos que lo forman son iguales.
                                Habrá máximo 20 puntos en la entrada.
    Valor a imprimir:
    Cantidad de cuadrados encontrados. Todos los cuadrados que se deben contar son los que tienen un lado paralelo al eje x y otro lado paralelo al eje y. Cualquier cuadrado que no cumpla eso no se debe contar.

    TEST CASE:
    Input: ["0,0","0,3","3,0","3,3"]
    Output: 1
    
    Input: ["0,0","0,3","3,0","3,3","3,5","5,3","5,5"]
    Output: 2
    
    Input: ["0,0","0,3","3,0","3,3","3,5","5,3","5,5","0,5","5,0"]
    Output: 3
    
    Input: ["0,0","0,3","3,0","3,3","3,5","5,3","5,5","5,0","8,0","8,3"]
    Output: 3
    
    Input: ["0,0","2,0","4,0","2,2","2,4","4,2","4,4","5,4","5,2","0,6","0,4","4,6","6,4","6,6","6,0"]
    Output: 6
    '''
    
str_coord=["0,0","2,0","4,0","2,2","2,4","4,2","4,4","5,4","5,2","0,6","0,4","4,6","6,4","6,6","6,0"]
list_coord=[]
cont=0
i=0
k=0

for str in str_coord:
    list_coord.append(str.split(","))
#print(list_coord)

for list in list_coord:
    
    while i<len(list_coord)-1:
        nexti=list_coord[i+1]
        #print(list,nexti)
        punto1=[list[0],nexti[1]]
        punto2=[nexti[0],list[1]]
        #print(punto1)
        #print(punto2)
        if ((int(list[0])-int(nexti[0]))+int(nexti[1]))==int(list[1]) and ((int(nexti[0])-int(list[0]))+int(list[1]))==int(nexti[1]) or abs((int(list[0])-int(nexti[0]))-int(nexti[1]))==int(list[1]) and abs((int(nexti[0])-int(list[0]))-int(list[1]))==int(nexti[1]):  #((int(list[0])-int(nexti[0]))+int(nexti[1]))==int(list[1]) or abs((int(list[0])-int(nexti[0]))-int(nexti[1]))==int(list[1]): 
            if list[0]!=nexti[0] and list[1]!=nexti[1]:
                if punto1 in list_coord and punto2 in list_coord:
                    cont+=1
        i+=1
    k+=1
    i=k
    
print(f"cuadrados:{cont//2}")

#Codigo
