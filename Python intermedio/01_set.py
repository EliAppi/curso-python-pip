#Conjuntos - set
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

print("*"*10) #Separador manual de operaciones

set_numbers = {1, 2, 2, 443, 23} #Elimina numeros repetidos
print(set_numbers)

print("*"*10) #Separador manual de operaciones

set_types = {1, 'hola', False, 12.12} #Ordena aleatoriamente
print(set_types)

print("*"*10) #Separador manual de operaciones

set_from_string = set('hoola') #convierte string en set
print(set_from_string)

print("*"*10) #Separador manual de operaciones

set_from_tuples = set(('abc', 'cbv', 'as', 'abc')) #convierte tupla en set
print(set_from_tuples)

print("*"*10) #Separador manual de operaciones

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)

