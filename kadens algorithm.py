# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums=list(map(int,input().split()))
global_max=0
curr_sum=0
for i in range(len(nums)):
    curr_sum=max(curr_sum+nums[i],nums[i])
    global_max=max(global_max,curr_sum)
print(global_max)