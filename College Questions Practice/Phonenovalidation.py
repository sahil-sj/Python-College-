# a="hardware hardware"
# print(a.rfind('a'))
from itertools import count
pno=input("Enter phone no: ")
if pno[0]=='6' or pno[0]=='7' or pno[0]=='8' or pno[0]=='9':
    if len(pno)==10:
        for i in pno:
            if pno.count(i)>7:
                print("Invalid String. A digit in phone no can't be repeated more than 7 times")
                break
        else:
            print("Valid Strig")
    else:
        print("Inavlid String. No of digits in phone no should be greater than 10.")
else:
    print("Invalid string. Phone No should start either with '6' or '7' or '8' or '9'") 