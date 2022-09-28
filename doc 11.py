n=int(input("enter the no:"))
s=0
i=n
while n>0:
    a=n%10
    s=s+a
    n=n//10
print(s)