a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
min=1
max=0
n=[]
k=[]
while i<len(a):
    if max<len(a[i]):
        max=len(a[i])
        n=a[i]
    if min>=len(a[i]):
        min=len(a[i])
        k=a[i]
    i+=1
print("max=",max,n)
print("min=",min,k)
# c=0
# while i<len(n):
#     j=0
#     c1=0
#     while j<len(n[i]):
#         j+=1
#         c1+=1
#     i+=1
# c+=1
# print("max=",(c1,n[-1]))
# print("min=",(c,n[0]))