class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while not (n & 0b1):
            n = n >> 1
        return n == 1
