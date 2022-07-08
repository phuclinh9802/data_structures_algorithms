# is unique:  Implement an algorithm to determine
# if a string has all unique characters. What if you
# cannot use additional data structures?

# since we check if characters in a string are not duplicated
# we can use a boolean hash map to check if that character
# already exists

def is_unique(string):
    # ASCII -> we have base case: string length > 128 => return false
    if len(string) > 128:
        return False

    # else, we first initialize a hash_map
    # -> space complexity: O(N)
    # then go through the string
    string_hash_map = {}

    # go through the string
    for c in string:
        # check if c is already in hash map
        if c in string_hash_map:
            return False
        else:
            string_hash_map[c] = True

    return True

# Time Complexity: O(N) - N: length of string
# Space Complexity: O(128) - O(1)
print(is_unique('abn'))


# ------------- Better solution with O(1) space complexity -------------
# ------------ Hint: Bit Manipulation --------------