# n=(input("enter a number"))
# i=0
# add=""
# while i<len(n):
#   add=add+n[i]
#   j=1
#   while j<=(len(n)-(i+1)):
#     add+="0"
#     j+=1
#   if i==(len(n)-1):
#     pass
#   else:
#     add+="+"
#   i+=1
# print(add)

n=(input("enter a number"))
l=len(n)
i=0
while i<l:
  print(int(n[i])*(10**((l-1)-i)),"+",end="")
  i+=1
  
