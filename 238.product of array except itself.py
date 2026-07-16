# 238.product of array except itself
nums=[3,4,1,2]
n=len(nums)
ans=[1]*n
prefix=1
for i in range(n):
    ans[i]*=prefix
    prefix=prefix*nums[i]
suffix=1
for i in range(n-1,-1,-1):
    ans[i]=ans[i]*suffix
    suffix*=nums[i]
print(ans)
    