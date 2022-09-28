str=input("enter the name:")
len=len(str)
r=0
while r<=len-1:
    c=0
    while c<=r:
        print(str[c],end="")
        c=c+1
    r=r+1
    print()
    