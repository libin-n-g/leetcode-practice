class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count_ones = 0
        if n < 1:
            return False
        while n:
            count_ones += (n & 0b1)
            n = n >> 1
        return count_ones == 1
