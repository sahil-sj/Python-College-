def insertionsort(l):
    for i in range(1,len(l)):
        j=i-1
        while j>=0 and l[j]>l[i]:
            (l[j],l[i])=(l[i],l[j])
            i=j
            j=j-1

    return l

l=[76,54,87,90,32]
s=insertionsort(l)
print(s)     