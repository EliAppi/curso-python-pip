numbers=[1,2,3,4]
numbers_v2=[]
for x in numbers:
  numbers_v2.append(x*2)

print(numbers)
print(numbers_v2)

#Lo mismo de arriba con map y lambda
numbers_v3=list(map(lambda x: x*2, numbers))
print(numbers_v3)

print("*"*10) # Separador manual de operaciones


#Otro ejemplo con map y lambda - Suma entre listas
numbers_1=[1,2,3,4]
numbers_2=[5,6,7]

result=list(map(lambda x,y: x+y, numbers_1,numbers_2))

print(numbers_1)
print(numbers_2)
print(result)