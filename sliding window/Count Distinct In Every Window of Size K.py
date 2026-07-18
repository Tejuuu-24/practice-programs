# Count Distinct In Every Window of Size K
nums = list(map(int, input().split()))
k = int(input())

freq = {}
res = []

# First window
for i in range(k):
    freq[nums[i]] = freq.get(nums[i], 0) + 1

res.append(len(freq))

# Sliding window
for i in range(k, len(nums)):
    left = nums[i-k]

    freq[left] -= 1
    if freq[left] == 0:
        del freq[left]

    freq[nums[i]] = freq.get(nums[i], 0) + 1

    res.append(len(freq))

print(res)


