# n=[4,6,4,3,3,4,3,4,6,6]
# k=2
# a=[]
# i=0
# while i<len(n):
#     b=n[i]
#     j=0
#     c=0
#     while j<len(n):
#         if n[i]==n[j]:
#             c+=1
#         j+=1
#     if c>k:
#         if b not in a:
#             a.append(b)
#     i+=1
# print(a)

i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    i+=1
    print()