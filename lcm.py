# a=int(input())
# b=int(input())
# # n=max(a,b)
# while b:
#     a,b=b,a%b
# print(a)

# import math
# print(math.gcd(3,6))
a=int(input())
b=int(input())
m=max(a,b)
while True:
    if m%a==0 and m%b==0:
        print(m)
        break
    else:
        m+=m




