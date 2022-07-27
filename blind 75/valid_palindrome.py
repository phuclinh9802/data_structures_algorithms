class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #         # base case
        #         if len(s) <= 1:
        #             return True

        #         result = ""
        #         s = s.replace(' ', '')
        #         for c in s:
        #             if c.isalnum() == False and c != ' ':
        #                 s = s.replace(c, '')
        #                 continue
        #             result = c + result

        #         return lower(result) == lower(s)

        if len(s) <= 1:
            return True

        i, j = 0, len(s) - 1

        while i <= j:
            # skip non-alphanumeric characters
            if s[i].isalnum() == False or s[j].isalnum() == False:
                if s[i].isalnum() == False:
                    i += 1
                if s[j].isalnum() == False:
                    j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1

        return True





