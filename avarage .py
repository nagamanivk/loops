# n=int(input("enter the no:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print(sum/n,"is the avg")

n=int(input("enter the no:"))
i=1
while i<=n:
    j=1
    while j<=10:
        print(i,"*",j,"=",i*j)
        j=j+1
    i=i+1
    print()