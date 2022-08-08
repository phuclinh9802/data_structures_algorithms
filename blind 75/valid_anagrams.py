class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # if unicode characters
        # i = 0
        # store_s = ''
        # store_t = ''
        # while i < len(s):
        #     if s[i].isalnum() == False and t[i].isalnum() == False:
        #         i += 1
        #     elif s[i].isalnum() and t[i].isalnum() == False:
        #         store_t += t[i]
        #     elif s[i].isalnum() == False and t[i].isalnum():
        #         store_s += s[i]
        #     else:
        #         store_t += t[i]
        #         store_s += s[i]
        #     i += 1

        # return sorted(store_s) == sorted(store_t)
        return sorted(s) == sorted(t)