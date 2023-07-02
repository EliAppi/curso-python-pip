sentence="Welcome to CodeWars"
    # Your code goes here
rev_list_sent=[]
list_sent=sentence.split(" ")
print(list_sent)
for x in list_sent:
    if len(x)>=5:
        list_x=",".join(x).split(",")
        list_x.reverse()
        x="".join(list_x)
    rev_list_sent.append(x)
    #rev_list_sent.append(x)
print(rev_list_sent)