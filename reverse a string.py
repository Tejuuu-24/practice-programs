# reverse a string
s=input()
left=0
r=len(s)-1
while left<r:
    s[left],s[r]=s[r],s[left]
    left+=1
    r-=1
print(s)