n=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
a=[]
while i<(len(n)):
    a.append([n[i],n[i+1],n[i+2]])
    i+=3
    # a.append([n[i],n[i+1],n[i+2],n[i+3],n[i+4]])
    # i+=5
print(a)
