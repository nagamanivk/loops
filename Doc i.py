n=int(input("enter the no:"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i+1
    print()

# n=int(input("no"))
# i=5
# while i>=n:
#   print(str(i)*i)
# i=i-1
# print()
    