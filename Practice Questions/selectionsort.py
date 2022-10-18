# def selectionsort(l):
#     for i in range(len(l)):
#             pos=i
#             for j in range(i+1,len(l)):
#                 if l[j] < l[pos]:
#                     pos=j
#             (l[i],l[j]) = (l[j],l[i])
#     return(l)
def selectionsort(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]<l[i]:
                pos=j
        (l[i],l[pos])=(l[pos],l[i])
    return(l)

         
l=[12,8,1,3,6,4]
my=selectionsort(l)
print(my)
