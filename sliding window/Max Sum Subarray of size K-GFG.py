# Max Sum Subarray of size K
arr=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(k):
    sum+=arr[i]
max_sum=sum
for i in range(k,len(arr)):
    sum+=arr[i]-arr[i-k]
    max_sum=max(max_sum,sum)
print(max_sum)