# n=[1,2,3,1,2,3,4]
# i=0
# c=0
# a=[]
# while i<len(n):
#     j=0
#     while j<len(n)-1:
#         if n[i]==n[j]:
#             c+=1
#             if n[i] not in a:
#                 a.append([str(n[i])*c])
#         j+=1
#     i+=1
# print(a)


# list=[1,4,67,89,34,56,2,6,7]
# prime=[]
# for i in list:
#     c=0
#     for j in range(1,i):
#         if i%j==0:
#             c+=1
#     if c==1:
#         prime.append(i)
# print(prime)

# prime=[]
# for i in range(1,100):
#     c=0
#     for j in range(1,i):
#         if i%j==0:
#             c+=1
#     if c==1:
#         prime.append(i)
# print(prime)

# i=0
# while i<5:
#     print(i,end="")
#     j=0
#     while j<=8:
#         if (i==0 and j==4) or (i==1 and j in {3,5}) or (i==2 and j in {2,6}) or (i==3 and j in {1,7}) or (i==4 and j%2==0):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#         j+=1
#     i+=1
#     print()


# n=input("enter a number")
# i=0
# l=len(n)
# while i<=0:
#     if l%2==0:
#         print("even")
#     else:
#         print("odd")
#     i+=1


# n=int(input("enter a number"))
# sum=0
# i=1
# while i<=n:
#     a=((n//100)%10)*100
#     b=((n//10)%10)*10
#     c=n%10
#     i+=1
# print(a,"+",b,"+",c)

n=[1,2,3,[4,5,6,[7,8,9],10]]
i=0
a=[]
sum=0
while i<len(n):
    if type(n[i])==list:
        j=0
        while j<len(n[i]):
            if type(n[i][j])==list:
                k=0
                while k<len(n[i][j]):
                    a.append(n[i][j][k])
                    sum+=n[i][j][k]
                    k+=1
            else:
                a.append(n[i][j])
                sum+=n[i][j]
            j+=1
    else:
        a.append(n[i])
        sum+=n[i]
    i+=1
print(a)
print(sum)