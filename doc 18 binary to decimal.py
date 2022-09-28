from re import I


n=int(input("enter the no:"))
a=0
i=1
while n>0:
    r=n%10
    a=a+r*i
    i=i*2
    n=int(n/10)
print(n)