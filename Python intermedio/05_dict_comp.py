#Ejemplo 
dict = {}
for i in range(1, 5):
  dict[i] = i * 2
print(dict)

#Comprension de dictionary
dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)

print("*"*10) #Separador manual de operaciones


#Ejemplo random
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 100) #valor random int
print(population)

#dictionary comprehension
population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

print("*"*10) #Separador manual de operaciones


#Ejemplo
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(set(zip(names, ages))) #zip hace union entre una list y otra

#dictionary comprehension
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)