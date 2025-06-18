class Solution:

    @staticmethod
    def power(x, p):
        if p == 0:
            return 1
        if p % 2 == 0:
            result = power(x, p // 2)
        else:
            result = power(x, p // 2) * x * power(x, p // 2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        MOD = 10**9 + 7
        i = 0
        max_len = 0
        m = set()
        for j, s_j in enumerate(s):
            while s_j in m:
                m.remove(s[i])
                i +=1
            m.add(s_j)
            max_len = max(max_len, len(m))
        return max_len

        