n=int(input())
for i in range(1,n):
    sum=i/(i*i)
    print(f"{i}/{i*i} + ",end="")
print(f"{n}/{n*n} = {sum}") 