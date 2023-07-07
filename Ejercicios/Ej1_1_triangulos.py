''' Enunciado: Encontrar cuántos triángulos rectángulos hay en un conjunto de puntos. Recuerde que un triángulo rectángulo es un triángulo que tiene un ángulo recto.
    Argumentos: Array de String
    Condiciones de la entrada:  Todos los puntos dados por (x, y) son coordenadas enteras con números no negativos menores o iguales a 1000. No habrá dos puntos repetidos en la entrada. 
                                Todos los triángulos rectángulos que se deben contar son los que tienen dos lados paralelos a cada uno de los ejes. 
                                Dos triángulos son considerados iguales si los tres puntos que lo forman son iguales.
                                Habrá máximo 20 puntos en la entrada.
    Valor a imprimir:
    Cantidad de triángulos rectángulos encontrados. Todos los triángulos rectángulos que se deben contar son los que tienen un lado paralelo al eje x y otro lado paralelo al eje y. Cualquier triángulo que no cumpla eso no se debe contar. Por ejemplo:
    Input: ["0,0","2,2","0,4"]
    Output: 0

    TEST CASE:
    Input: ["0,0","0,3","0,6","3,0","6,0"]
    Output: 4
    
    Input: ["2,0","2,2","2,4","2,10","2,12","1000,14","2,14","3,14","4,14","5,14"]
    Output: 20
    
    Input: ["0,0","0,3","3,3","0,6"]
    Output: 2
    
    Input: ["0,0","0,3","3,3","3,0","6,0","3,6"]
    Output: 7
    '''


str_coord=["0,0","0,3","3,0"]
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
        if list[0]!=nexti[0] and list[1]!=nexti[1]:
            punto1=[list[0],nexti[1]]
            punto2=[nexti[0],list[1]]
            #print(punto1)
            #print(punto2)
            if punto1 in list_coord or punto2 in list_coord:
                cont+=1
                #print(cont)
        i+=1
    k+=1
    i=k
    
print(cont)