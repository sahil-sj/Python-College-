n=int(input())
sum=0
for i in range(1,n):
    sum+=i*i
    print(f"{i*i} + ",end="")
print(f"{n*n} = {sum}")