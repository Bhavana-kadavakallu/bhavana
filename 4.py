l=[1,2,2,5,8,4,4,8]
i=0
a=[]
c=0
while i<len(l):
    if l[i] not in a:
        a.append(l[i])
        c+=1
    i+=1
print(c)