# l1=[10,20,30,40]
# l2=[100,200,300,400]
# i=0
# while i<len(l1):
#     j=3
#     while j>=0:
#         print(l1[i],l2[j])
#         j-=1
#         i+=1

# a=[1,'f',2,'b',3,4,'h','j',6,9,0,'k']
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if type(a[i])==str:
#         b.append(a[i])  
#     else:
#         c.append(a[i])
#     i+=1
# print(b)
# print(c)

# n=[0,9,5]
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         k=0
#         while k<len(n):
#             if i!=j and j!=k and i!=k:
#                 print(n[i],n[j],n[k])
#             k+=1
#         j+=1
#     i+=1

# l=[1,2,[3,2,[5,6],3,[4]],89,80]
# i=0
# sum=0
# a=[]
# while i<len(l):       
#     if type(l[i])==list:
#         j=0
#         while j<len(l[i]):
#             if type(l[i][j])==list:
#                 k=0
#                 while k<len(l[i][j]):
#                     a.append(l[i][j][k])
#                     sum+=l[i][j][k]
#                     k+=1
#             else:
#                 a.append(l[i][j])
#                 sum+=l[i][j]
#             j+=1
#     else:
#         a.append(l[i])
#         sum+=l[i]
#     i+=1
# print(a)
# print(sum)

# n=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# while i<len(n):
#     c=max(n)
#     b=min(n)
#     i+=1
# print(c)
# print(b)
# i=0
# c=0
# while i<len(n):
#     j=0
#     c1=0
#     while j<len(n[i]):
#         j+=1
#         c1+=1
#     i+=1
# c+=1
# print("max=",(c1,max(n)))
# print("min=",(c,min(n)))

# n=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
# i=0
# while i<len(n):
#     a=max(n)
#     i+=1
# print(a)
# i=0
# sum=0
# sum1=0
# sum2=0
# sum3=0
# max=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if i==0:
#             sum+=n[i][j]
#         elif i==1:
#             sum1+=n[i][j]
#         elif i==2:
#             sum2+=n[i][j]
#         else:
#             sum3+=n[i][j]
#         j+=1
# #     i+=1
# # print(sum,sum1,sum2,sum3)
#     if n[i]>max:
#         max=n[i]
#     i+=1
# 
# qqqqqq print(max)

# n=[22.4,4.0,16.22,9.1,11.0,12.22,14.2,5.2,17.5]
# i=0
# max=0
# min=n[i]
# while i<len(n):
#     if n[i]>max:
#         max=n[i]
#     elif n[i]<min:
#         min=n[i]
#     b=int(n[i])*5
#     print(b,end=" ")
#     i+=1
# print("max=",int(max))
# print("min=",int(min))
# b.sort()
# print(b)
# n.sort()


# n=["red","white","blue","green","orange"]
# m=["black","yellow","green","blue"]
# i=0
# a=[]
# b=[]
# while i<len(n):
#     if n[i] not in m:
#         a.append(n[i])
#         j=0
#         while j<len(m):
#             if m[j] not in n:
#                 b.append(m[j])
#             j+=1
#         # break
#     i+=1
# print(a)
# print(b)

# n=["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
# i=0
# a=[]
# b=[]
# c=[]
# while i<len(n):
#     if i%3==0:
#         a.append(n[i])
#     elif n[i] not in a:
#         # if i%3==0:
#         b.append(n[i])
#     i+=1
# print(a)
# print(b)


n=[[1,2,3],[3,4,5],[1,1,1]]
i=0
while i<len(n):
    a=min(n)
    i+=1
    print(a)


# loops

# n=int(input("enter a number of bits"))
# i=n
# while n!=0:
#     if n%4==0:
#         print("good")
#     else:
#         print("not good")
#     break
#     i+=1

# n=int(input("number of students want to enroll"))
# m=int(input("max number of students"))
# x=int(input("already enrolled students"))
# i=n
# while n>0:
#     if x+n<=m:
#         print("yes")
#     else:
#         print("no")
#     break
#     i+=1

# n=int(input("total minutes"))
# m=int(input("decide to spent munites"))
# i=n
# while n>0:
#     a=m/2
#     b=n-m
#     if (a+b)%2==0:
#         print(int(a+b))
#         break
#     i+=1

# n=int(input("total litres contain in tank"))
# m=int(input("number of bottles"))
# k=int(input("each bottle contain litres"))
# i=n
# while n>0:
#     a=n/k
#     print("no of bottles=",(a))
#     print("remaining=",(m-a))
#     break
#     i+=1



