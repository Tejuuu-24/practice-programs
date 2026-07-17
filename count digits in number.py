# count digits in number
n=int(input())
count=0
while n>0:
    count+=1
    n//=10
print(count)
# TC-O(log n)
