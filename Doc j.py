# n=int(input("enter the no:"))
# i=1
# while i<=n:
#     k=1
#     while k<=n-i:
#         print(" ",end="")
#         k=k+1
#     j=i
#     while j>=1:
#         print(j,end=" ")
#         j=j-1
#     i=i+1
#     print()


n=int(input("enter the no:"))
i=5
while i>n:
    k=1
    while k>=i-n:
        print(" ",end="  ")
        k=k-1
    j=1
    while j<=i*2-1:
        print("*",end= "  ")
        j=j+1
    i=i-1
    print()
    


              
