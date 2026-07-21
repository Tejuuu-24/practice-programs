# find is given array sorted or not
nums=[5,7,11,13]
valid=True
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        valid=False
if valid:
    print("array is sorted")

        

