n=['0', '1', '2', '3', '4']
m=['red', 'green', 'black', 'blue', 'white']
a=['100', '200', '300', '400', '500']
i=0
b=[]
while i<len(n):
    j=0
    while j<len(m):
        k=0
        while k<len(a):
            if i==j==k:
                b.append(n[i]+m[j]+a[k])
            k+=1
        j+=1
    i+=1    
print(b)