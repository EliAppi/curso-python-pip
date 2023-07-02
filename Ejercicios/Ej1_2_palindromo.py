import re
string="oso"
list_string=re.findall("[A-Za-z]+",string.lower())
new_string="".join(list_string)
list_cont=[]
poli=[]
k=0
i=1
j=1
print(new_string)

for x in new_string:
    list_cont.append(new_string.count(x))
print(list_cont)

while j<len(new_string):
    for x in list_cont:
        mitad=list_cont.index(x)
        if x==i and mitad!=0:
            print("index mitad",mitad)
            print("len",len(new_string))
            
            while mitad<len(new_string)-1: #len(new_string)=3
                if list_cont[mitad-i]==list_cont[mitad+i]:
                    poli.append(new_string[mitad+i])
                else:
                    break
            i+=1
    j+=1
            

print(poli)    
print(len(poli)*2+1)

'''print(list_string)
print(new_string)
list_cont=[]
palindromo=[]
i=0

for x in new_string:
    list_cont.append(new_string.count(x))

print(list_cont)

for y in list_cont:
    if y>=2:
        palindromo.append(new_string[i])
    i+=1    
print(palindromo, len(palindromo))'''