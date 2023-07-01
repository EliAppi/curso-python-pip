nombre="Eli"
apellido="Piñeros"
print (nombre+" "+apellido) 

escapar_backslash='I\'m Ivory' 
print(escapar_backslash)


template1="Hola, mi nombre es "+nombre+" y mi apellido es "+apellido
print(template1)

#Uso de formato para string
template2="Hola, mi nombre es {} y mi apellido es {}".format(nombre,apellido) #.format
print(template2)

template3=f"Hola, mi nombre es {nombre} y mi apellido es {apellido}" #f
print(template3)