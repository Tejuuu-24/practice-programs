def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):                                  # 5 4 2 1
    res=[]                                            #5 4      2 1
    l=0
    r=0
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            res.append(left[l])
            l+=1
        else:
            res.append(right[r])
            r=-1
    res.extend(left[l:])
    res.extend(right[r:])
    return res
nums=[5,4,2,1]
print(merge_sort(nums))

            

        