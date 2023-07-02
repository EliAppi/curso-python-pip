arr=[1]
import functools
    
elegido=0
print(arr)

if arr==[]:
    print (-1)
else:
    while(elegido<len(arr)):
        der=arr[elegido+1:]
        izq=arr[:elegido]
        print(f"elegido:{elegido} rango der: {der} rango izq: {izq}")
        
        if len(arr)==1:
            print (0)
            break
        elif der==[]:
            suma_der=0
            suma_izq=functools.reduce(lambda a,b:a+b,izq)
        elif izq==[]:
            suma_izq=0
            suma_der=functools.reduce(lambda a,b:a+b,der)
        else:
            suma_der=functools.reduce(lambda a,b:a+b,der)
            suma_izq=functools.reduce(lambda a,b:a+b,izq)
                
        print(f"suma derecha: {suma_der} suma izq:  {suma_izq}")
        if suma_der==suma_izq:
            print(f"index elegido: {elegido}")
            break
        elif elegido==len(arr)-1:
            print(-1)
            break
        elegido+=1
        

'''#Reducido eli con metodo sum
arr=[1,2,3,4,5,4,3,2,1]
elegido=0
print(arr)

if arr==[]:
    print (-1)
else:
    while(elegido<len(arr)):
        der=arr[elegido+1:]
        izq=arr[:elegido]
        print(f"elegido:{elegido} rango der: {der} rango izq: {izq}")
        
        if sum(der)==sum(izq):
            print(f"index elegido: {elegido}")
            break
        elif elegido==len(arr)-1:
            print(-1)
            break
        elegido+=1'''


#Reducido codigo otros
'''def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

resultado=find_even_index([1,2,2,3,4,5,3])
print(resultado)'''