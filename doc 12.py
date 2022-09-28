n=int(input("enter the no:"))
f=1
i=n
while n>0:
    a=n%10
    f=f*a
    n=n//10
print(f)

