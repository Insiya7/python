n=int(input("Enter a Amount"))
m=input("Enter a loyalty")
d=(95*n)/100
d1=(80*n)/100
d2=(85*n)/100
if m=="basic":
    print("The discount wil be",d)
elif m=="premium":
    print("The discount wil be",d1)
elif m=="vip":
    print("The discount wil be",d2)
else:
    print("invalid")
    
