# min Sum Subarray of size K
arr=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(k):
    sum+=arr[i]
min_sum=sum
for i in range(k,len(arr)):
    sum+=arr[i]-arr[i-k]
    min_sum=min(min_sum,sum)
print(min_sum)