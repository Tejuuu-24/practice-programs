# inp=paypal is hiring
str="paypalishiring"
n=3
if n==1 or n>len(str):
    print(str)
rows=[" "]*n
currow=0
d=-1  #up or down
for ch in str:
    rows[currow]+=ch
    currow+=1
    if currow==0 or currow==n-1:
        d*=-1
    currow+=d
print("".join(rows))

