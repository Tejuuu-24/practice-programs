#count all digits
num = int(input())
rev = 0
original=num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
if rev==original:
    print("palindrome")
else:
    print("not a palindrome")