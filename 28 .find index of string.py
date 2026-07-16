haystack="sadbutsad"
needle="sad"
# if needle in haystack:
#     print(haystack.find(needle))

n=len(needle)
for i in range(len(haystack)-n+1):
    if haystack[i:i+n]==needle:
        print(i)
        break
    else:
        print(-1)

# (OR)

if needle in haystack:
    print(haystack.find(needle))