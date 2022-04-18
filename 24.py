n=[1,2,3,2,4,7,2,1]
i=0
a=[]
while i<len(n):
    if n[i] not in a:
        a.append(n[i])
    i+=1
print(a)