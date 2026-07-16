# 2965
nums=[[1,3],[2,2]]
repeated,missing=0,0
freq={}
n=len(nums)
for i in nums:
    for j in i:
        if j in freq:
            freq[j]+=1
        else:
            freq[j]=1
for i in range(1,(n*n)+1):
    if i in freq:
        if freq[i]==2:
            repeated=i
    else:
        missing=i
print([repeated,missing])




