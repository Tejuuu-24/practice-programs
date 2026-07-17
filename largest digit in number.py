#largest digit in number
num=int(input())  #12543
l=0
while num>0:
    digit=num%10
    if digit>l:
        l=digit
    num//=10
print(l)
