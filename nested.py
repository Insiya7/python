"""rain = 0
umb = 1
if rain:
    if umb:
        print("Go to school")
    else:
        print("Don't go to school.")
else:
    print("Go to school.")"""

a = 1
b = 456
c = 12

if a>b:
    if a>c:
        print(a)
        if c>b:
            print(c)
            print(b)
        else:
            print(b)
            print(c)
    else:
        print(c)
        print(a)
        print(b)
else:
    if b>c:
        print(b)
        if c>a:
            print(c)
            print(a)
        else:
            print(a)
            print(c)
    else:
        print(c)
        print(b)
        print(a)
        
