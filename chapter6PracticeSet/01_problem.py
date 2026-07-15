a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
d=int(input("Enter the number"))


if(a>b and a>c and a>d):
    print("A is greater")


elif(b>c and b>d):
    print("B is greater")

elif(c>d):
    print("C is greater")
else:
    print("D is greater")
