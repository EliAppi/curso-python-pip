''' Enunciado: Dado un texto, encontrar la subcadena palíndroma más larga
    Argumentos: Una cadena de texto.
    Condiciones de la entrada:  Tendrá al menos un símbolo y estará compuesto sólo por espacios, puntos y letras del alfabeto inglés.
                                Para este problema puede ignorar los espacios, mayúsculas/minúsculas y los puntos. Ver los ejemplos para más claridad.
                                Valor a imprimir: La longitud de la subcadena palíndroma más larga. Recordar que una cadena palíndroma, es una cadena que se lee igual al derecho que al revés, como:
    “ Os  o” = 3
    “Radar” = 5
    “civic” = 5
    
    TEST CASE:
    Input: "xxAbc cb a x y z"
    Output: 8
    
    Input: "Una frase con una palindroma Anita lava la tina muy muy larga"
    Output: 15
    
    Input: "A b cde"
    Output: 1
    
    Input: "ggrrrrrrrrRRRRrrrrgg anita lava la tina aJI TRAGA LA LAGARTIJA" 
    Output: 20
    '''

import re
string="A b cde" 
list_string=re.findall("[^. ]+",string.lower()) #Obvia puntos y espacios
new_string="".join(list_string)
#list_cont=[]
list_palindromo=[]
list_len_palindromo=[]
mayor=0
mayor2=0

i=1
j=1

if len(string)>1:
    while i<len(new_string)-1: 
        a=i-1
        b=i+1
        #print(f"a:{a}, medio:{i}, b:{b}")
            
        if new_string[a]==new_string[b]:
            j=i
            while j<len(new_string)-1:
                #print(f"rango izq: {new_string[a:i]}, rango der: {new_string[i+1:b+1]}")
                list_der=list(new_string[i+1:b+1])
                list_der.reverse()
                rev_der="".join(list_der)
                #print(f"izq: {new_string[a:i]}, der: {rev_der}") 
                if new_string[a:i]==rev_der:                    #comparando por letras | no por repeticiones
                    list_palindromo.append(new_string[a:b+1])
                    a-=1
                    b+=1
                j+=1
        i+=1
    #print(list_palindromo)    

    if list_palindromo!=[]:
        
        for y in list_palindromo:
            list_len_palindromo.append(len(y))
            mayor=max(list_len_palindromo)
        #print(mayor)
        index_mayor=list_len_palindromo.index(mayor)
        #print(list_palindromo[index_mayor])
    
    #print("Palindomo es par")
    i=1
    j=1
    list_palindromo2=[]
    list_len_palindromo2=[]
    #print("Segunda oportunidad")
    #print(new_string)


    while i<len(new_string): 
        a=i-1
        b=i
        #print(f"a:{a}, medio:{i}, b:{b}")
            
        if new_string[a]==new_string[b]:
            j=i
            while j<len(new_string):
                #print(f"rango izq: {new_string[a:i]}, rango der: {new_string[i:b+1]}")
                list_der=list(new_string[i:b+1])
                list_der.reverse()
                rev_der="".join(list_der)
                #print(f"izq: {new_string[a:i]}, der: {rev_der}") 
                if new_string[a:i]==rev_der:
                    list_palindromo2.append(new_string[a:b+1])
                    a-=1
                    b+=1
                j+=1
        i+=1
    #print(list_palindromo2) 

    if list_palindromo2!=[]:
        for y in list_palindromo2:
            list_len_palindromo2.append(len(y))
            mayor2=max(list_len_palindromo2)
        #print(mayor2)
        index_mayor2=list_len_palindromo2.index(mayor2)
        #print(list_palindromo2[index_mayor2])
        
    if list_palindromo==[] and list_palindromo2==[]:
        print(0)
    else:
        if mayor>mayor2:
            print(mayor)
            print(list_palindromo[index_mayor])
        else:
            print(mayor2)
            print(list_palindromo2[index_mayor2])       

    
    
elif len(string)==1:  
    print(1)  
else:
    print(0)