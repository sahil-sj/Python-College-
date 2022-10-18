a=input("Enter string : ")
c=input("Enter chracter : ")
if c in a:
    for i in a:
        if c==i:
            print(c)
            break
        else:
            print(i,end="")
else:
    print("Chracter not found ")

