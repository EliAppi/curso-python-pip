num=int(input("Ingresa un entero: "))
i=0
patron=["***","*Q*","***"]
new_arr=[]

for x in patron:
    repeticion="*"+x[1]*num+"*"
    new_arr.append(repeticion)
#print(new_arr)

while(i<num-1):
    new_arr.insert(1,new_arr[1])
    i+=1
    
print(new_arr)