class Solution:
    def appealSum(self, s: str) -> int:
        appeal_sum = 0
        n = len(s)
        last_occurance = {}
        for i in range(n):
            c = s[i]
            if c in last_occurance:
                appeal_sum += (i - last_occurance[c]) * (n-i)
            else:
                appeal_sum += (i + 1) * (n-i)
            last_occurance[c] = i
        return appeal_sum