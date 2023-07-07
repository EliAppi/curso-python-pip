#INCOMPLETO Encuentra el palindromo mas largo
#Funciona con palindromos que tienen numero impar de caracteres
import re
string="oso acca in alylani"
list_string=re.findall("[^. ]+",string.lower()) #Obvia pountos y espacios
new_string="".join(list_string)
list_cont=[]
list_palindromo=[]
list_len_palindromo=[]
i=1
j=1

for x in new_string:
    list_cont.append(new_string.count(x))
print(new_string)
print(list_cont)

while i<len(list_cont)-1: 
    a=i-1
    b=i+1
    #print(f"a:{a}, medio:{i}, b:{b}")
        
    if new_string[a]==new_string[b]:
        j=i
        while j<len(list_cont)-1:
            print(f"rango izq: {list_cont[a:i]}, rango der: {list_cont[i+1:b+1]}")
            print(f"rango izq: {new_string[a:i]}, rango der: {new_string[i+1:b+1]}")
            if sum(list_cont[a:i])==sum(list_cont[i+1:b+1]):
                list_palindromo.append(new_string[a:b+1])
                a-=1
                b+=1
            j+=1
    i+=1
print(list_palindromo)

if list_palindromo==[]:
    print(1)
else:
    for y in list_palindromo:
        list_len_palindromo.append(len(y))
        mayor=max(list_len_palindromo)
    print(mayor)
    index_mayor=list_len_palindromo.index(mayor)
    print(list_palindromo[index_mayor])