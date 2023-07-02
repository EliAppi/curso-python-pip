str_coord=["2,0","2,2","2,4","2,10","2,12","1000,14","2,14","3,14","4,14","5,14"]
list_coord=[]
cont=0
i=0
k=0

for str in str_coord:
    list_coord.append(str.split(","))
#print(list_coord)

iterable=iter(list_coord)
pos0=next(iterable)
#print(pos0)

for list in list_coord:
    
    while i<len(list_coord)-1:
        nexti=list_coord[i+1]
        #print(list,nexti)
        if list[0]!=nexti[0] and list[1]!=nexti[1]:
            #print("diferente")
            cont+=1
        i+=1
    k+=1
    i=k
    
print(cont)