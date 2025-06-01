class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for i in range(min(limit, n) + 1):
            count += max(min(n-i, limit) - max(0, n-i-limit) + 1, 0)
        return max(count, 0)