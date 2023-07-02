import functools
strText=input("Ingresa numeros en texto separado por espacios: ")
strNum=["zero","uno","dos","tres","cuatro","cinco"]
list_num=[]
suma=0

list_str=strText.split(" ")
print(list_str)

for x in list_str:
    for y in strNum:
        if x==y:
            list_num.append(strNum.index(x))
            break
        
print(list_num)

print(functools.reduce(lambda a, b: a+b, list_num))