# subsets
nums=[1,2,3]
n=len(nums)
res=[[]]
for num in nums:
    newsub=[]
    for subset in res:
        newsub.append(subset+[num])
    res.extend(newsub)
print(res)