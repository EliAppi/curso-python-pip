#Ejemplo 
numbers = []
for element in range(1, 11):
  numbers.append(element * 2)
print(numbers)

print("*"*10) #Separador manual de operaciones

#Comprension de lista
numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

print("*"*10) #Separador manual de operaciones

#Otro ejemplo + if
numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)
print(numbers)

print("*"*10) #Separador manual de operaciones

#Comprension de lista + if
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)