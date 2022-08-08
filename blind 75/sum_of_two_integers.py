def sum_integers(a, b):
    # use binary operations
    # base case: 32-bit
    bit32 = 0xffffffff

    # when b = 0
    a = a & bit32

    while b != 0:
        # get sum first
        sum = (a^b) & bit32
        carry = ((a&b) << 1) & bit32
        a = sum
        b = carry

    # negative case
    if (a >> 31) & 1:
        a = ~(a^bit32)

    return a