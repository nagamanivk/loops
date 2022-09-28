
 

i=1
r=5
c=5
while i<=r:
    j=1
    while j<=c:
        if i==1 and j==3 or i==2 and j==2 or i==2 and j==4 or i==3 and j==1 or i==3 and j==5 or i==4 and j==2 or i==4 and j==4 or i==5 and j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()


i=1 
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    m=2

    while m<=i:
        print(m,end="")
        m=m+1
    i=i+1
    print()