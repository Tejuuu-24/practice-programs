# anagram
a="tea"
b="ate"
def find_a(m):
    freq={}
    for i in m:
        freq[i]=freq.get(i,0)+1
    return freq
if (find_a(a)==find_a(b)):
    print("true")
else:
    print("false")