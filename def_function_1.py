def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def multipy(num1,num2):
    print(num1*num2)
def divide(num1,num2):
    print(num1/num2)
num1=int(input("enter the first no"))
opr=input("enter operation")
num2=int(input("enter the second no"))
if opr=="+":
    r=add(num1,num2)
elif opr=="-":
    r=sub(num1,num2)
elif opr=="*":
    r=multiply(num1,num2)
elif opr=="/":
    r=divide(num1,num2)
else:
    r="invalid operator"
print(r)

