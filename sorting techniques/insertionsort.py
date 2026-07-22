# insertion sort
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]     
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]   
            j -= 1
        arr[j + 1] = temp #11 12 5 6 13 
    return arr

arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))