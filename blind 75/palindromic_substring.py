class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        res_2 = []

        for i in range(len(s)):
            # odd case
            tmp = self.helper(s, res, i, i)

            # even case
            tmp = self.helper(s, res, i, i + 1)

        for n in res:
            if len(n) > 1:
                res_2.append(n)

        return len(s) + len(res_2)

    # get palindromic substring
    def helper(self, s, res, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            tmp = s[l + 1:r]
            if len(tmp) > 1:
                res.append(s[l + 1:r])

        return s[l + 1:r]


