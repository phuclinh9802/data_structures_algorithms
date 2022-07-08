# URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13
# Output: "Mr%20John%20Smith"

# we can use the method of two-scan approach
# first, we count the # of valid whitespaces
# then, we can replace those whitespaces with %20 and we want to go backward
# to avoid override

def urlify(string, length):
    str_list = list(string)
    # first, we want to count the valid whitespaces
    white_space = 0
    for i in range(length):
        if string[i] == ' ':
            white_space += 1

    # then, we can get rid of whitespaces after the actual string
    str_len = len(string)
    if str_len > length:
        for i in range(length, str_len):
            str_list[i] = ''

    string = "".join(str_list)
    print(string)
    # then, we can replace valid whitespaces with %20
    string = string.replace(' ', '%20')

    return string

print(urlify('Mr John Smith ', 13))




