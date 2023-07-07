#INCOMPLETO Encuentra cuadrados en coordenadas dadas
#En prueba FALLANDO
str_coord=["0,0","0,3","3,0","3,3","8,0","8,3","6,0","6,3"]
list_coord=[]
cont=0
i=0
k=0
list_result_h=[]
list_result_v=[]

for str in str_coord:
    list_coord.append(str.split(","))
print(list_coord)

for lista in list_coord:
    
    while i<len(list_coord)-1:
        nexti=list_coord[i+1]
        print(lista,nexti)
        
        if int(lista[0])==int(nexti[0]):
            #list_result.append("h") 
            list_result_h.append(abs(int(lista[1])-int(nexti[1]))) #(int(lista[1])-int(nexti[1])))
            #print(list_result_h)
            
        elif int(lista[1])==int(nexti[1]):
            #list_result.append("v") 
            list_result_v.append(abs(int(lista[0])-int(nexti[0]))) #(int(lista[0])-int(nexti[0])))
            #print(list_result_v)
                
        i+=1
    k+=1
    i=k
    
print(list_result_v)   
print(list_result_h)

if len(list_result_v)>=len(list_result_h):
    #iterable_v=iter(list_result_v)
    set_h=set(list_result_h)
    for h in set_h:
        repet=list_result_v.count(h)
        if repet>=2:
            cont+=1
elif len(list_result_v)<len(list_result_h):
    #iterable_v=iter(list_result_v)
    set_v=set(list_result_v)
    for v in set_v:
        repet=list_result_h.count(v)
        if repet>=2:
            cont+=1               
        
  
print(f"cuadrados:{cont}") #Debo comparar horizontales con verticales y contar las veces q se repiten
#print(list_list) 
#print(list(map(lambda x,y:x+y,[0,3],[3,0])))

'''print(list(map(lambda x,y:x-y,[0,3],[3,0])))
print(list(map(lambda x,y:x+y,[0,3],[3,0])))
print(list(map(lambda x,y:x+y,[6,0],[3,6])))
print(list(map(lambda x,y:x+y,[0,0],[3,6])))
print(list(map(lambda x,y:x+y,[3,0],[0,6])))
print(list(map(lambda x,y:x+y,[0,0],[3,6])))'''