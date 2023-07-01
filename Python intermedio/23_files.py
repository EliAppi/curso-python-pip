file=open('./text.txt') #Abre el archivo

#print(file.read())  #Puede ser pesado cuando hay mucha informacion en el text.txt
print(file.readline()) #Paso a paso lees la linea de text.txt
print(file.readline())
print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

file.close() #Cierra el archivo para desocupar memoria

print("*"*10) # Separador manual de operaciones


#Lo mismo de arriba pero con instruccion para abrir y cerrar archivo automaticamente 
with open('./text.txt') as file: 
  for line in file:  #Muestra todas las lineas tambien ocupa mucha memoria
    print(line)