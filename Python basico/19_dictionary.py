my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "aeronave",
  'name': 'Eli',
  'last_name': 'Piñeros',
  'age': 31
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))

print('avion' in my_dict)
print('otroqueno' in my_dict)


print("*"*10)
#CRUD
person = {
  'name': 'Eli',
  'last_name': 'Piñeros',
  'langs': ['python', 'javascript'], #Puede contener array interno
  'age': 31
}

print(person)

person['name'] = 'Alex' #Reemplazando valores
person['age'] -= 50 #Resto 50 al primer valor (31)
person['langs'].append('rust') #añado skill al final del array
print(person)

print("*"*10)

del person['last_name'] #Elimino key y valor
person.pop('age') #Elimino key y valor
print(person)


print("*"*10) # Separador manual de operaciones

print('items')  #imprime todos los item del diccionario en tuplas
print(person.items())

print('keys') # imprime todas las key del diccionario en tuplas
print(person.keys())

print('values') #Imprime todos los valores del diccionario en tuplas
print(person.values())