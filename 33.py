n=[12,67,98,34]
i=0
while i<len(n):
    j=0
    while j<len(n[i]):
        print(n[i][j]) 
        j+=1
    i+=1
# n=[15,81,11,234]
# i=0
# b=[]
# while i<len(n):
#     a=n[i]%10
#     n[i]=n[i]//10
#     c=a+n[i]
#     b.append(c)
#     i+=1
# print(b)