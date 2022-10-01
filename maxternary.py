import datetime
a,b,c=input("Enter a, b, c\n").split()
a=eval(a)
b=eval(b)
c=eval(c)
max=a if a>b and a>c else b if  b>c else c   
# max = (a if a>c else c) if(a>b) else(b if b>c else c)
print(max)

# dict={"a":5,"b":2