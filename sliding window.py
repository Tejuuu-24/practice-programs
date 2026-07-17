# sliding window
n=[1,2,3,4,5,6]
k=3
winsum=0
for i in range(k):
    winsum+=n[i]
maxsum=winsum
for i in range(k,len(n)):
    winsum=winsum+n[i]-n[i-k]
    maxsum=max(maxsum,winsum)
print(maxsum)

