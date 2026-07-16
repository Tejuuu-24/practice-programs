# maximum sum of distinct subarrays with len k
nums=[1,5,4,2,9,9,9]
k=3
s=set()
window_sum=0
max_sum=0
l=0
for r in range(len(nums)):
    while nums[r] in s or (r-l+1)>k:
        window_sum-=nums[l]
        s.remove(nums[l])
        l+=1
    s.add(nums[r])
    window_sum+=nums[r]
    if (r-l+1)==k:
        max_sum=max(window_sum,max_sum)
print(max_sum)


