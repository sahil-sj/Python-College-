def prime(n):
    count=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            print("No is not prime\n")
            count=1
            break
    if count==0:
        print("no is prime")

prime(23)