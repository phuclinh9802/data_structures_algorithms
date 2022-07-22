# list of sorting/searching algorithms
# sorting: bubble, selection, insertion, mergesort, quicksort
# searching: binary search

def bubble(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# [3,2,1,4,0] -> 3 min ->
def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

# [3,2,1,4,0] -> pick 2 -> 2 < 3 -> arr[1] = 3, arr[0] = 3
def insertion(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current

    return arr

arr = [3, 2, 1, 4, 0]
# print(bubble(arr))
# print(selection(arr))
print(insertion(arr))

# merge sort