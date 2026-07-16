# inp=paypal is hiring
str="paypalishiring"
n=3
rows=[" "]*n
currow=0
d=-1
for ch in str:
    rows[currow]+=ch
    currow+=1
    if currow==0:
        d*=-1
    currow+=dir
print(currow)

