n=[1,2,3,4,5,6,7,8,9,10]
i=0
a=[]
while i<(len(n)-1):
    a.append(n[i+1]-n[i])
    i+=1
print(a)

# n=[2,4,6,8]
# i=0
# a=[]
# while i<(len(n)-1):
#     a.append(n[i+1]-n[i])
#     i+=1