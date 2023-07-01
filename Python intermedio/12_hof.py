def increment(x):
  return x + 1

def high_ord_func(x, func):
  return x + func(x) # 2 + (2 + 1)

result = high_ord_func(2, increment)
print(result) #5


#Lo mismo de arriba pero con Lambda
increment_v2 = lambda x: x+1

high_ord_func_v2 = lambda x,func: x+func(x)  # 2 + (2 + 1)

result = high_ord_func_v2(2, increment_v2)
print(result) #5

#Creando lambdas sobre la marcha
result = high_ord_func_v2(2, lambda x: x+2) # 2 + (2 + 2)
print(result)
## change
result = high_ord_func_v2(2, lambda x: x*5) # 2 + (2 * 5)
print(result)