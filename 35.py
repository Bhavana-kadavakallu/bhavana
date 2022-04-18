n=[1234,122,1984,19372,100]
a=list(n)
b=a[0]
c=0
i=0
print((a[i][0]))
while i<len(a):
    if a[i][0]==b[0]:
        c+=1
    i+=1
if c==len(a):
    print("true")
else:
    print("false")

# a=["abd","anhd","akoy","arty"]
# b=a[0]
# i=0
# c=0
# while i<len(a):
#     if a[i][0]==b[0]:
#         c+=1
#     i+=1
# if c==len(a):
#     print("true")
# else:
#     print("false")