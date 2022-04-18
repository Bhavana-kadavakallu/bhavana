# n=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# i=0
# a=[]
# b=4
# while i<len(n):
#     if i==b:
#         a.append(20)
#         b+=4
#     a.append(n[i])
#     i+=1
# print(a)

n=['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
i=0
a=[]
b=3
while i<len(n):
    if i==b:
        a.append("z")
        b+=3
    a.append(n[i])
    i+=1
print(a)