n=[[1,1,1,1],2]
i=0
a=[]
while i<len(n):
    j=0
     while j<len(n[i]):
        if n[j]==n[j+1]:
             a.append(n[j])
        j+=1
    i+=1
print(a)




