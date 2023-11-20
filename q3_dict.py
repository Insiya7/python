a=[['yellow',1],['blue',2],['yellow',3],['blue',4],['red',1]]
d=dict()
for i in range (0,len(a)):
    if a[i][0] not in d:
        d[a[i][0]] = [a[i][1]]
    else:
        d[a[i][0]].append(a[i][1])

print(d)
