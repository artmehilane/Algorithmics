def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Testin koodi
print(binary_search(sorted_array, 9))
print(binary_search(sorted_array, 8))
