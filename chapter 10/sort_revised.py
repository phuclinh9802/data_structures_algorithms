# bubble sort

# best case: O(n)
# avg case: O(n^2)
# worst case: O(n^2)
# space: O(1)

def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# best case: O(n^2)
# avg case: O(n^2)
# worst case: O(n^2)
# space: O(1)
def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[min], arr[i] = arr[i], arr[min]

    return arr

# best case: O(n)
# avg case: O(n^2)
# worst case: O(n^2)
# space: O(1)
def insertion(arr):
    for i in range(1, len(arr)):
        element = arr[i]
        j = i - 1
        while j >= 0 and element < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = element

    return arr

arr = [3,2,1,4,0]
# print(bubble(arr))
# print(selection(arr))
# print(insertion(arr))

# note: get left arr and right arr, then recursively call merge_sort of left arr and merge_sort right arr to traverse to only one element in a subarray
# Best case: O(nlogn)
# Avg case: O(nlogn)
# Worst case: O(nlogn)
# Space: O(n)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            elif right_arr[j] < left_arr[i]:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# merge_sort(arr)
# print(arr)


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)

def partition(arr, start, end):
    # define pivot being the last el of the array
    pivot = arr[end]
    # define stored index
    storedIndex = start - 1

    for i in range(start, end):
        # if current element < element at pivot, increment storedIndex, then swap current element with stored index element
        if arr[i] < pivot:
            storedIndex += 1
            arr[i], arr[storedIndex] = arr[storedIndex], arr[i]

    arr[storedIndex+1], arr[end] = arr[end], arr[storedIndex+1]

    return storedIndex + 1

quick_sort(arr, 0, len(arr) - 1)
print(arr)