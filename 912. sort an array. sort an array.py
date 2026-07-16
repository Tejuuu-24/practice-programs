# 912. sort an array
nums=[3,5,1,2]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j]<nums[i]:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)
