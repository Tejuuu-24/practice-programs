nums=[1,1,2,2,2,3,3,3]
l=0
r=0
while r<len(nums):
    if nums[l]==nums[r]:
        r+=1
    else:
        nums[l+1],nums[r]=nums[r],nums[l+1]
        l+=1
        r+=1
print(nums)