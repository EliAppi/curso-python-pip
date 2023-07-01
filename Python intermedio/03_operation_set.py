set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b) #con metodo
print(set_c)
print(set_a | set_b) #Con operador

set_c = set_a.intersection(set_b) #con metodo
print(set_c)
print(set_a & set_b) #Con operador

set_c = set_a.difference(set_b) #con metodo
print(set_c)
print(set_a - set_b) #Con operador

set_c = set_a.symmetric_difference(set_b) #con metodo
print(set_c)
print(set_a ^ set_b) #Con operador