x=3.3
print(x)
y=1.1+2.2
print(y)
print(x==y)

y_str=format(y,".2g") #Limito el float a dos digitos pero se convierte en string
print(y_str)
print(y_str == str(x))

print("*"*20)

print(y,x)
tolerance=0.00001 #Creo margen de tolerancia para que la comparacion sea verdadera
print(abs(x-y)<tolerance)

print("*"*20)

print(y==x)
print(round(y,1)==x) #round, redondea el numero a la cantidad de decimales que yo quiera
