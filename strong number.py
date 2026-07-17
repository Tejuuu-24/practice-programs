# strong number - sum of factorial of digits
n=int(input()) #145
sum=0
original=n
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    n//=10
if sum==original:
    print("strong number")
else:
     print("not strong number")
