#Ejemplo random
import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

print("*"*10) #Separador manual de operaciones


#Ejemplo + if
result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

print("*"*10) #Separador manual de operaciones


#Ejemplo + if
text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' } #Convierto vocales en text en mayusculas y hago un diccionario con ellas
print(unique)

print("*"*10) #Separador manual de operaciones


#Ejemplo conteo de vocales
text = "Hola a todos, esta es una cadena de texto de prueba."
print(text)
unique = { c: text.count(c) for c in text if c in 'aeiou' }
print(unique)#f"unique: {unique}")