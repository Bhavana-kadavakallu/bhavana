n= [5, 6, [], 3, [], [], 9]
i=0
a=[]
while i<len(n):
    if n[i]!=[]:
        a.append(n[i])
    i+=1
print(a)