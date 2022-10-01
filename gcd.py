# print("hello")
# x=6
# z='hello'
# print(type(z))
# list1=[1,'hello',76.9]
# print(list[2])
# # list2=list1
# list2=list1[ : ]
# list1[1]=344
# print(list1)
# print(list2)
def gcd(m,n):
    i=min(m,n)
    while(i>0):
        if(m%i==0 and n%i==0):
            return i
        else:
            i=i-1

y=gcd(14,63)
print(y)






