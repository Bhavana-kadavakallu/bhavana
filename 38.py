n="https://www.w3resource.com/python-exercises/list/"
i=0
a=n.split(" ")
b=" "
print(a)
m=['.com', '.edu', '.tv']
while i<len(a):
    j=0
    while j<len(m):
        if a[i]==m[j]:
            print("true")
        else:
            print("false") 
        j+=1
    i+=1