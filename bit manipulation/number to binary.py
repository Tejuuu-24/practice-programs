n=13
res=" "
while n>0:
    if n%2==1:
        res+='1'
    else:
        res+='0'
    n//=2
print(res[::-1])