# Find the average of every window of size K. 
nums=list(map(int,input().split()))
k=int(input())
sum=0
res=[]
for i in range(k):
    sum+=nums[i]
res.append(sum/k)
for i in range(k,len(nums)):
    sum+=nums[i]-nums[i-k]
    res.append(sum/k)
print(res)