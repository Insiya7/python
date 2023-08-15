num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
opr=input("Enter a opr")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("Invalid opr")
