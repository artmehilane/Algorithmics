def linear_search(arr, x):

    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1

array = [15, 33, 45, 80, 14, 19]
search_value = 45

print(linear_search(array, search_value))

