user=input("enter your words: ")
i=0
l=[]
while i<len(user):
    if user[i] not in l:
        l.append(user[i])
    i=i+1
j=0
while j<len(l):
    k=0                                   ##### list question
    c=0
    while k<len(user):
        if user[k]==l[j]:
            c=c+1
        k=k+1
    print(l[j],c)
    j=j+1
    
    

