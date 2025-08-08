class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = len(s)
        for i in range(n):
            # odd palamdrome stating with i
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if len(res) < r - l + 1:
                    res = s[l:r+1]
                r += 1
                l -= 1

            # even palandrome stating with i and i + 1
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if len(res) < r - l + 1:
                    res = s[l:r+1]
                r += 1
                l -= 1
        return res