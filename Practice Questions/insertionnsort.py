def insertionsort(l):
    for i in range(len(l)):
        j=i
        while j>0 and l[j]<l[j-1]:
            (l[j],l[j-1])=(l[j-1],l[j])
            j=j-1

    return l

l=[76,54,87,90,32]
s=insertionsort(l)
print(s)     