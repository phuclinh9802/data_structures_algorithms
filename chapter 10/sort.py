# 1
# Bubble Sort:
# best case: O(n) - when they are all sorted
# avg case: O(n^2)
# worse case: O(n^2)
# review:
# [3, 2, 1, 4, 0] ->  compare between adjacent elements j & j+1
def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [3,2,1,4,0]


# best case: O(n^2) - when they are all sorted
# avg case: O(n^2)
# worse case: O(n^2)
def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

# arr = bubble(arr)


# best case: O(n) - when they are all sorted
# avg case: O(n^2)
# worse case: O(n^2)
def insertion(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

    return arr



# best case: O(nlogn) - when they are all sorted
# avg case: O(nlogn)
# worse case: O(nlogn)
# space: O(n)
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
            elif left_arr[i] > right_arr[j]:
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

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)

def partition(arr, start, end):
    pivot = arr[end]
    index = start - 1

    for i in range(start, end):
        print('stored index:', index, 'current:', i, 'first')
        if arr[i] <= pivot:
            # swap between i and index
            print(index, i)
            index += 1
            arr[i], arr[index] = arr[index], arr[i]
        print('arr', arr)


    # swap between pivot point and the current stored index
    arr[end], arr[index+1] = arr[index+1], arr[end]
    print('swap: stored index:', index+1, 'end:', end)
    print('new arr:', arr)
    return index + 1

# merge_sort(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
