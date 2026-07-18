# Check if any window of size K has all distinct elements
nums = list(map(int, input().split()))
k = int(input())

freq = {}

# First window
for i in range(k):
    freq[nums[i]] = freq.get(nums[i], 0) + 1

if len(freq) == k:
    print(True)
else:
    found = False

    # Slide the window
    for i in range(k, len(nums)):
        left = nums[i-k]

        freq[left] -= 1
        if freq[left] == 0:
            del freq[left]

        freq[nums[i]] = freq.get(nums[i], 0) + 1

        if len(freq) == k:
            found = True
            break

    print(found)