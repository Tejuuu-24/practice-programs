# a=int(input())
# b=int(input())
# # n=max(a,b)
# while b:
#     a,b=b,a%b
# print(a)

# import math
# print(math.gcd(3,6))
# -----recursion-----
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(8,6))





