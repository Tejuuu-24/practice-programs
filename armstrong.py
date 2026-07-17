#armstrong num  range
def armstrong(n):
    digits=len(str(n))
    arm=0
    original=n
    while n>0:
        digit=n%10
        arm+=digit**digits
        n//=10
    return arm==original
def arm_range(start,end):
    for i in range(start,end+1):
        if armstrong(i):
            print(i)
start=int(input())
end=int(input())
print(arm_range(start,end))

