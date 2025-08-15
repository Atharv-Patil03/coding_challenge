def sort012(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1


    while mid <= high:
        if arr[mid] == 0:
            # swap 
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # 1 is in the middle
            mid += 1
        else:
            # swap 
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1


data = [0, 1, 2, 1, 0, 2, 1, 0]
sort012(data)
print(data)   
