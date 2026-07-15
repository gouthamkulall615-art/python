a=int(input("Enter ur agg for the voter list:"))
#if elif ladder

if(a>=18):
    print("You are eligible for voting")
elif(a<0):
    print("enter ur correct age for the validation")

elif(a==0):
    print("your are age is zero")
else:
    print("you are not eligible for voting")


print("End of the code")