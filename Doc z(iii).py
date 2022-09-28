# n=int(input("enter the no:"))
# i=5
# while i>=n:
#     k=5
#     while k>=i-n:
#         print(" ",end="")
#         k=k-1
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     i=i-1
#     print()
 
#  n=int(input("enter the number of rows:"))
# i=0
# while i<3:
#     j=0
#     while j<3:
#         print(1+j, end=" ")
#         j+=1
#     i+=1
#     print()

# i=250
# while i<=259:
#     j=248
#     if j<i:
#         print(i-j)
#     j-=1
#     i+=1


n=int(input("enter the no:"))
i=0
while n>0:
    r=n%10
    i=i+r
    n=n//10
print("sum is:",i)