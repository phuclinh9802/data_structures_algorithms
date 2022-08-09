def longest_wo_repeating_char(s):
    # base case
    if len(s) == 0:
        return 0

    res = 0
    store = ""
    i = 0

    for i in range(len(s) - 1):
        store = s[i]
        for j in range(i + 1, len(s)):
            if s[j] not in store:
                store += s[j]
                res = max(res, len(store))
            else:
                break

    return res
