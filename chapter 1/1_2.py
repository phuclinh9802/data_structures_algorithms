# Check Permutation: Given two strings, write a method
# to decide if one is a permutation of the other

# we can sort both strings then compare if they are equal

# merge sort
def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def string_permutation(str1, str2):
    arr1 = list(str1)
    arr2 = list(str2)

    merge_sort(arr1)
    merge_sort(arr2)

    str1 = "".join(arr1)
    str2 = "".join(arr2)

    return str1 == str2

# -------------------- better approach ------------------
# -------------------- hash table -------------------
def string_permutation_optimized(str1, str2):
    # base case
    if len(str1) != len(str2):
        return False

    # hash map
    hash_map = {}

    for c in str1:
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1

    for c in str2:
        # check if c is in hash_map
        if c in hash_map:
            hash_map[c] -= 1

        if hash_map[c] < 0:
            return False

    return True


print(string_permutation_optimized('aaca', 'aacc'))



