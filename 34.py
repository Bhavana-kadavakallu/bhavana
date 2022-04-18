n= [34.67, 12, -94.89, 'Python', 0, 'C#']
i=0
a=[]
while i<len(n):
    if type(n[i])==int:
        a.append(n[i])
    i+=1
print(a)