#funcion normal con return
def increment(x):
  return x + 1
result = increment(10)
print(result)

#lo mismo de arriba con funcion lambda
increment_v2 = lambda x: x + 1

result = increment_v2(20)
print(result)


#funcion lambda para texto
full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('eli', 'piñeros')
print(text)