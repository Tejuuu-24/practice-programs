# 1480. Running Sum of 1d Array
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
nums=list(map(int,input().split()))
prefix=[0]*len(nums)
prefix[0]=nums[0]
for i in range(1,len(nums)):
    prefix[i]=nums[i]+prefix[i-1]
print(prefix)
