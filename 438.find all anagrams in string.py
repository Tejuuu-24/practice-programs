# 438.find all anagrams in string
s="cbaeacbda"
p="abc"
win_sum={}
s_win={}
res=[]
for i in p:
    win_sum[i]=win_sum.get(i,0)+1
for i in range(len(p)):
    s_win[s[i]]=s_win.get(s[i],0)+1
if s_win == win_sum:
    res.append(0)
for i in range(len(p),len(s)):
    left=s[i-len(p)]
    s_win[left]-=1
    if s_win[left] == 0:
        del s_win[left]

    s_win[s[i]] = s_win.get(s[i], 0) + 1

    if s_win == win_sum:
        res.append(i - len(p) + 1)
print(res)
    

