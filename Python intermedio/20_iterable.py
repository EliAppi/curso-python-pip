for i in range(1, 10): #Modo automatico
  print(i)


my_iter = iter(range(1, 4)) #Modo manual
print(my_iter)
print(next(my_iter)) #1
print(next(my_iter)) #2
print(next(my_iter)) #3
print(next(my_iter)) #Error por exceder el rango de iterable