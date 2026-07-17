# string to int
x="151"
ans=0
for ch in x:
    ans=ans*10+ord(ch)-ord('0')
print(ans)

# #int to string
# # int to string
# x = 152
# res = ""

# while x > 0:
#     digit = x % 10
#     x = x // 10
#     res = chr(ord('0') + digit) + res

# print(res)
# print(type(res))
