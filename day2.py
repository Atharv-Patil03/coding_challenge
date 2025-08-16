def find_missing_number(arr):

    n = len(arr) + 1

    total = n * (n + 1) // 2
    current_sum = 0
    for num in arr:
        current_sum += num
      
    missing = total - current_sum
    return missing

# test cases
print(find_missing_number([1, 2, 4, 5]))   # 3
print(find_missing_number([2, 3, 4, 5]))   # 1
print(find_missing_number([1, 2, 3, 4]))   # 5
print(find_missing_number([1]))            # 2
