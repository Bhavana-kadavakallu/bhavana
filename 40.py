# n=[[1, 2, 4], [2, 4, 4], [1, 2]]
n=[[1], [2, 4, 4], [1, 2], [4]]
i=0
sum=0
sum1=0
sum2=0
a=[]
while i<len(n):
    j=0
    while j<len(n[i]):
        if j==0:
            sum+=n[i][j]
        elif j==1:
            sum1+=n[i][j]
        else:
            sum2+=n[i][j]
        j+=1
    i+=1
a.append(sum)
a.append(sum1)
a.append(sum2)
print(a)