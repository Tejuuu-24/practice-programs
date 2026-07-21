n=2
c=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        c+=1
        if i!=n//i:
            c+=1
if c==2:
    print("prime")
else:
    print("not prime")
