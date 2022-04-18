import random
list1=["python","list","exercises","practice","solution"]
b=[]
for i in list1:
    a=list(i)
    random.shuffle(a)
    a="".join(a)
    b.append(a)
print(b)