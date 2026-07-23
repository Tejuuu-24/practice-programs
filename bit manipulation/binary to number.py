n="1101"
power=1
res=0
for i in range(len(n)-1,-1,-1):
    if n[i]=='1':
        res+=power

    power*=2
print(res)
