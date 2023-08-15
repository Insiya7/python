s=int(input("Enter a Amount"))
amt=(5*s)/100
amt2=(10*s)/100
amt3=(15*s)/100
if s<50000:
    print("the tax is",amt)
elif s>=50000 and s<=100000:
    print("the tax is",amt2)
else:
    print("the tax is",amt3)
