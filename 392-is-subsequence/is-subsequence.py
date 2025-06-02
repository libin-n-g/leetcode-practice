class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_index, t_index = 0, 0
        while t_index < len(t):
            if t[t_index] == s[s_index]:
                s_index += 1
            if s_index == len(s):
                return True
            t_index += 1
        return False