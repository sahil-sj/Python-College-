# print("hello bro")
# def mystery(l):
#     l=l[2: ]
#     return(l)
# mylist = [7,11,13,17,19,21]
# print(mystery(mylist))  
# s="anaconda"
# e=""
# for i in range(1,len(s)):
#     e=e+s[i]
# print(e)
# l = [7,11,13,17,19,21]
# a = l
# print(a)
# if a is l:
#     print("true")
# else:

#     print("false")
def selectionsort(l):
    for i in range(len(l)):
        pos=i
        for j in range(i+1,len(l)):
            if l[j]<l[pos]:
                pos=j
        (l[i],l[pos])=(l[pos],l[i])
    return(l)

         
l=[12,8,1,3,6,4]
my=selectionsort(l)
print(my)
