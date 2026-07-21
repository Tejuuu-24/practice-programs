# median
arr=list(map(int,input().split()))
n=len(arr)
if n%2!=0:
    print(arr[n//2])
else:
    print((arr[n//2]+(arr[n//2]-1))//2)


    