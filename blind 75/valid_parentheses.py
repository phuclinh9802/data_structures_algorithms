class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hash_map = {'}': '{', ']': '[', ')': '('}
        stack = []

        if len(s) == 1:
            return False

        for c in s:
            if c in hash_map.values():
                stack.append(c)
            elif c in hash_map:
                if stack == [] or hash_map[c] != stack.pop():
                    return False

        return stack == []

