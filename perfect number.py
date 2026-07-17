# perfect number
n=int(input()) #28
if n == 1:
    exit()
c=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        c+=i
        if i!=n//i and n//i!=n:
            c+=n//i
if c==n:
    print("perfect num")
else:
    print(" not perfect num")
