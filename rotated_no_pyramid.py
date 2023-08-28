x = 1
a = 5
for i in range(a,0,-1):
    x = i
    for j in range(0,a):
        if j>=a-i:
            print(f"{x} ",end="")
            x+=1
        else:
            print("  ",end="")
        
    print()
