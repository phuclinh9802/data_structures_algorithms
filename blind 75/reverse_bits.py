def reverse_bits(n):
    res = 0
    i = 0
    while i < 32:
        # move res to left to add 0 bit
        res = res << 1
        # increment res to n % 2
        res += n % 2
        # move n to the right
        n = n >> 1
        i += 1

    return res
