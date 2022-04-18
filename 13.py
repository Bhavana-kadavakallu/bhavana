a=[1,1,2,3,4,4,5,1]
a=str(a)
i=0
c=0
c1=0
c2=0
c3=0
c4=0
while i<len(a):
    if "1" in a[i]:
        c+=1
    elif "2" in a[i]:
        c1+=1
    elif "3" in a[i]:
        c2+=1
    elif "4" in a[i]:
        c3+=1
    elif "5" in a[i]:
        c4+=1
    i+=1
print([c,1],end=",")
print([c1,2],end=",")
print([c2,3],end=",")
print([c3,4],end=",")
print([c4,5])