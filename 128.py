# 128
nums=[100,4,200,1,3,2]
# if not nums:
#     print(0)
# nums.sort()
# longest=1
# curr=1
# for i in range(1,len(nums)):
#    if  nums[i]==nums[i-1]:
#        continue
#    elif nums[i]==nums[i-1]+1:
#        curr+=1
#        longest=max(curr,longest)
#    else:
#        curr=1
# print(longest)

"""optimized"""
longest=0
ns=set(nums)
for num in ns:  #9 1 100 2 101 3 102 4
    if num-1 not in ns:
        curr=num
        length=1
        while curr+1 in ns:
            curr+=1
            length+=1
        longest=max(longest,length)
print(longest)


