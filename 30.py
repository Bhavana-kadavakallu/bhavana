# n= [2, -7, 5, -64, -14]
n=[-12, 14, 95, 3]
i=0
c=0
c1=0
while i<len(n):
    if n[i]<0:
        c+=1
    else:
        c1+=1
    i+=1
print("pos=",c1)
print("neg=",c)
