x = 0.0
for i in range(10):
    x += 0.1

if x == 1.0:
    print(f'x = {x}')
else:
    print(f'x != {x}') #0.99999999999
    
#Para usar el numero con round  
numero = 1.234
con_dos_decimales = round(numero, 2)
print(con_dos_decimales)

#Para imprimir con formato
numero = 1.234
print("{:.2f}".format(numero)) # Salida: 1.23

#Imprimiendo una cadena con format
altura = 50.687
peso = 80.658412
print("Mi altura es {:.2f} y mi peso {:.2f}".format(altura, peso)) # Salida: Mi altura es 50.69 y mi peso 80.66