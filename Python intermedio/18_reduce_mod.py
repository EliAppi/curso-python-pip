import functools # modulo que permite hacer uso de counter e item como una operacion ya establecida y regresa el return para usar en el accum

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)
print(result)

print("*"*10) # Separador manual de operaciones


#Lo mismo de arriba con lambda
result = functools.reduce(lambda counter,item: counter+item, numbers)
print(result)