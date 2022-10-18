def mergesort(A,l,r):
    if l-r<=1:
        return (A[l:r])
    else:
        m=(l+r)//2