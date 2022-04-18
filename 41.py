n=[[1, 2], [2, 4]]
# n=[[0, 1, 2], [2, 4, 5]]
# n=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
i=0
c=0
c1=0
while i<len(n):
    c+=1
    j=0
    if i==0:
        while j<len(n[i]):
            c1+=1
            j+=1
    i+=1
print("(",c,end=",")
print(c1,")")