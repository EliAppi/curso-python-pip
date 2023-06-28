key="osiTO"
low_key=key.lower()
soup=["osito","OSito","wSIku","tnhqw","osito"]
iterador = iter(soup) #Debo definir con la funcion iter a soup para usar next

count=0
soup_list=[]
soup_hor_list=[]

for sou in soup:
    low_sou=sou.lower()     #Coloco en minusculas los textos a comparar
    if low_key==low_sou:    
        count+=1
   
   
                       
for k in low_key:
    for sou in soup:       
        low_sou=sou.lower()     #Coloco en minusculas los textos a comparar
        for s in low_sou:    
            if k==s:
                soup_list.append(k)
                break
        break

soup_str="".join(soup_list)
if low_key==soup_str:   
    count+=1

print(count)