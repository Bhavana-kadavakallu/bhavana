# n=[1,2,3]
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         k=0
#         while k<len(n):
#             if i!=j and j!=k and i!=k:
#                 print(n[i],n[j],n[k])
#             k+=1
#         j+=1
#     i+=1


n=[0,9,5]
i=0
while i<len(n):
    j=0
    while j<len(n):
        k=0
        while k<len(n):
            if i!=j and j!=k and i!=k:
                print(n[i],n[j],n[k])
            k+=1
        j+=1
    i+=1
