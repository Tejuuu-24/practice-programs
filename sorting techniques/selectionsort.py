nums=list(map(int,input().split()))
def selection_sort(nums):
    n=len(nums)
    for i in range(n):
        lower=i
        for j in range(i+1,n):
            if nums[j]<nums[lower]:
                lower=j
        nums[i],nums[lower]=nums[lower],nums[i]
selection_sort(nums)
print(nums)
