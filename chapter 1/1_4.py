# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)
# Hints: #106, #121, #134, #136
# page 91 - Solution: page 196

# we have to consider each condition
# even length: all characters appear in an even amount
# odd length: all characters except 1 character in the center appear in
# an even amount

def palindrome_permutation(string):
    # special cases:
    if len(string) == 1:
        return True

    if len(string) == 2:
        return string[0] == string[1]

    # we definitely need a hash map
    hash_map = {}

    for c in string:
        if c in hash_map:
            hash_map[c] += 1
        else:
            hash_map[c] = 1

    # odd case
    if len(string) % 2 == 1:
        count = 0
        for key, value in hash_map.items():
            # case where there are more than 1 odd character count
            if value % 2 == 1:
                count += 1
                if count > 1:
                    return False
        # case where there are no odd character
        if count == 0:
            return False

    # even case
    if len(string) % 2 == 0:
        count = 0
        for key, value in hash_map.items():
            if value % 2 == 1:
                count += 1

        if count >= 1:
            return False

    return True

print(palindrome_permutation('aabbccddeemf'))

# --------------- LET'S GO FIGURED OUT WITH ONLY ORIGINAL HINTS ------------------