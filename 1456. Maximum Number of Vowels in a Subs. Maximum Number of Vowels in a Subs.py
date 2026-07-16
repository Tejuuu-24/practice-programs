# 1456. Maximum Number of Vowels in a Substring of Given Length
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
k=3
s = "abciiidef"
vowels={'a','e','i','o','u'}
count=0
for i in range(k):
    if s[i] in vowels:
        count+=1
max_count=count
for i in range(k,len(s)):
    if s[i-k] in vowels:
        count-=1
    if s[i] in vowels:
        count+=1
    max_count=max(max_count,count)
print(max_count)
