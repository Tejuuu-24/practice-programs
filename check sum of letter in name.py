#check sum of digits in name
def check_sum(x):
    ans=0
    for ch in x:
        ans+=ord(ch)-ord('A')+1
    return ans
x=input().upper()
n=check_sum(x)
def armstrong(n):
    arm=0
    original=n
    digit=len(str(n))
    while n>0:
        digit=n%10
        arm+=digit*digit
        n//=10
    if original==arm:
        return "armstrong"
    else:
        return  "not armstrong"
print(armstrong(n))

