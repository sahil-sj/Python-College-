def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

# a=factorial(6)
# print(a)
print("the factorial of  is : ",factorial(6))
