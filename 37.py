# n=[1,2,3,4,5,6]
n=[1,2,3,4,5]
i=0
a=[]
while i<(len(n)-1):
    a.append([n[i],n[i+1]])
    i+=1
print(a)