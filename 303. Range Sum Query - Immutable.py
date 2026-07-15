# 303. Range Sum Query - Immutable


# Read array elements
arr = list(map(int, input().split()))

# Create prefix array
prefix = [0] * len(arr)

# First element
prefix[0] = arr[0]

# Build prefix sum array
for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

# Number of queries
q = int(input())

# Answer each query
for _ in range(q):
    left, right = map(int, input().split())

    if left == 0:
        print(prefix[right])
    else:
        print(prefix[right] - prefix[left - 1])