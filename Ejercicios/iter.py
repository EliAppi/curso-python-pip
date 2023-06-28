#iterables
iter('cadena') # cadena
iter(['a', 'b', 'c']) # lista
iter(('a', 'b', 'c')) # tupla
iter({'a', 'b', 'c'}) # conjunto
iter({'a': 1, 'b': 2, 'c': 3}) # diccionario

frutas ={'a': 1, 'b': 2, 'c': 3}
iterador = iter(frutas)
print(next(iterador))

print(next(iterador))

print(next(iterador))
