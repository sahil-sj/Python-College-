#M1
# a=input()
# c=0
# for i in a:
#     if i in "aeiouAEIOU":
#         c=c+1
# print("The no of vowels are : ",c)
# M2 using count
a=input("Enter string\n")
b="aeiouAEIOU"
s=0
for i in b:
    s+=a.count(i)
print("total: ",s)


