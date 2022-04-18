n=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
i=0
sum=0
sum1=0
sum2=0
sum3=0
sum4=0
c=0
c1=0
c2=0
c3=0
c4=0
a=[]
while i<len(n):
    j=0
    while j<len(n[i]):
        if j==0:
            sum+=n[i][j]
            c+=1
        elif j==1:
            sum1+=n[i][j]
            c1+=1
        elif j==2:
            sum2+=n[i][j]
            c2+=1
        elif j==3:
            sum3+=n[i][j]
            c3+=1
        else:
            sum4+=n[i][j]
            c4+=1
        j+=1
    i+=1
a.append([sum/c,sum1/c1,sum2/c2,sum3/c3,sum4/c4])
# a.append(sum1/c1)
# a.append(sum2/c2)
# a.append(sum3/c3)
# a.append(sum4/c4)
print(a)