l=[6,1,3,5,3,6,1]
i=0
a=[]
p=1
while i<len(l):
    if l[i] not in a:
        a.append(l[i])
        p=p*a[i]
    i+=1
print(p)