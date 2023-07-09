#import sys
#print(sys.path)
import random
aleatorio=random.randint(1, 100)
print (aleatorio)

import re
text="Mi numero de telefono es 321 456 7889, el codigo del pais es 57, mi numero de la suerte 3"
result=re.findall("[0-9]+",text)
print(result)

import time
timestamp=time.time()
local=time.localtime()
result=time.asctime()
print(result)

import collections
numbers = [1,1,2,1,5,4,3,5,5]
counter = collections.Counter(numbers)
print(counter)

import collections
numbers=["Anita lava la tina"]
new_numbers="".join(numbers)
lista=list(new_numbers)
counter=collections.Counter(lista)
print(counter)