# n= [4, 5, 5, 5, 3, 8]
# i=0
# while i<(len(n)-1):
#     if n[i]==n[i+1] and n[i+1]==n[i+2]:
#         print(n[i])
#     i+=1

n=[1,1,1,64,23,64,22,22,22]
i=0
# a=[]
while i<(len(n)-2):
    if n[i]==n[i+1] and n[i+1]==n[i+2]:
        # a.append(n[i])
        print(n[i],end=",")
    i+=1
# print(a)