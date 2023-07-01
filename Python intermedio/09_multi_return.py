#Funcion que me retorna multiples valores
def find_volume(length=2, width=1, depth=3): #Le pongo valores por defecto para poder enviar un solo parametro a la funcion
  return length * width * depth, width, 'hola'

result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)