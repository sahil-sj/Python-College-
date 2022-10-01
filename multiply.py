def multiply (m,n):
    if n==1:
        return m
    else:
        return m + multiply(m,n-1) 
    
a=multiply(23,6)
print(a)  



