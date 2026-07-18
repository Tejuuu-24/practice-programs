# 1004. Max Consecutive Ones III
nums=list(map(int,input().split()))
k=int(input())
left = 0
zeros = 0
ans = 0

for right in range(len(nums)):

    if nums[right] == 0:
        zeros += 1

    while zeros > k:

        if nums[left] == 0:
            zeros -= 1

        left += 1

    ans = max(ans, right - left + 1)

print(ans)