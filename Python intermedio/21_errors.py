#print(0 / 0) # Error no se puedn dividir numeros entre 0

#print(result) #Error result no esta definida

#suma = lambda x,y: x + y
#assert suma(2,2) == 8   #AssertionError - assert comprueba fallas


age = 10
if age < 18:
  raise Exception('No se permiten menores de edad') #Creo un error con raise Exception detiene programa

print('Hola 2')