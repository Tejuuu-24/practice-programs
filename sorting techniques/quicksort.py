# ?quicksort
def partitioning(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    while True:
        while i<=high and arr[i]<=pivot:
            i+=1
        while j>=low and arr[j]>pivot:
            j-=1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quick_sort(arr,low,high):
    if low<high:
        p=partitioning(arr,low ,high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

# Function call
quick_sort(arr, 0, n - 1)

# Output
print("Sorted array:", arr)
