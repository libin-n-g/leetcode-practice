class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ret = 0
        for i in range(k):
            if s[i] in 'aeiou':
                ret+=1
        max_ret = ret
        for i in range(k, len(s)):
            if s[i] in 'aeiou':
                ret+=1
            if s[i-k] in 'aeiou':
                ret-=1
            if ret > max_ret:
                max_ret = ret
        return max_ret