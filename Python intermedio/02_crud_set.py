set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

print("*"*10) #Separador manual de operaciones

# add
set_countries.add('pe') #agrega un elemento
print(set_countries)
set_countries.add('pe') #repetido no lo agrega
print(set_countries)

print("*"*10) #Separador manual de operaciones

# update
set_countries.update({'ar', 'ecua', 'pe'}) #agrega otro set
print(set_countries)

print("*"*10) #Separador manual de operaciones

# remove
set_countries.remove('col')
print(set_countries)

print("*"*10) #Separador manual de operaciones

set_countries.remove('ar')
set_countries.discard('arg') #Elimina pero si no lo encuentra no manda error
print(set_countries)
set_countries.add('arg')
print(set_countries)
set_countries.clear() #Vacia completamente el set
print(set_countries)
print(len(set_countries))