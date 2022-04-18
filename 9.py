a=[]
size=int(input("enter the size of list"))
for i in range(size):
    val=int(input("enter the value"))
    a.append(val)
max=a[0]
for i in range(size):
    if a[i]>max:
        max=a[i]
print(max)