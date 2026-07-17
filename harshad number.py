#  harshad / niven num
# divisible by its digit sum
# 18: 1+8=9, 
# 18%9=0. 
n=int(input())
original=n
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
if original%sum==0:
    print("Yes")
else:
    print("No")



