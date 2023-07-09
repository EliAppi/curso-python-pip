str_="Hello word"
#print(str_)
str_list=list(str_)
#print(str_list)
str_list2=list(str_)
#print(str_list2)
i=len(str_)-1
str_list3=[]

for letter in str_list2:
    #print(letter)
    str_list.append(letter)
    str_list.pop(0)
    temp_str="".join(str_list)
    #print(temp_str)
    str_list3.append(temp_str)   
        
print(str_list3)