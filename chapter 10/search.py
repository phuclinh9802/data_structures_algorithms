# binary search - Time: O(logn)

def binary_search(arr, start, end, x):
    if start < end:
        mid = start + (end - start) // 2
        if x < arr[mid]:
            # on the left
            mid = binary_search(arr, start, mid, x)
        elif x > arr[mid]:
            mid = binary_search(arr, mid + 1, end, x)
        else:
            return mid

    return -1

print(binary_search([1,2,3,4], 0, 4, 3))
