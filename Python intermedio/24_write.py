with open('./text.txt', 'w+') as file:   #'w+' Permiso read-write sobreescribiendo|| 'w' Permiso write || 'r' Permiso read || 'r+' Permiso read agregando nuevas lineas
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')
  file.write(' mas linea\n')
  
  
  