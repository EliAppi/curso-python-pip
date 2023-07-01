
for element in range(1, 5):
  print(element)

print("*"*10) # Separador manual de operaciones

my_list = [23, 45, 67, 89 ,43]
for element in my_list:
  print(element)

print("*"*10) # Separador manual de operaciones

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)

print("*"*10) # Separador manual de operaciones

product = {
  'name': 'Camisa',
  'price': 100,
  'stock': 89
}

for key in product:
  print(key, '=>', product[key])

for key, value in product.items():
  print(key, '=>', value)

print("*"*10) # Separador manual de operaciones

people = [
  {
    'name': 'nico',
    'age': 34
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print('name =>', person['name'])