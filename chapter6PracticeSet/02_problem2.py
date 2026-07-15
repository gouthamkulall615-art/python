m1=int(input("Enter the marks of the sub1"))
m2=int(input("Enter the marks of the sub2"))
m3=int(input("Enter the marks of the sub3"))

total_percentage=(100*(m1+m2+m3))/300

if(total_percentage>=40 and m1>33 and m2>33 and m3>33):
    print("Your are passed")
else:
    print("Your are failed!")