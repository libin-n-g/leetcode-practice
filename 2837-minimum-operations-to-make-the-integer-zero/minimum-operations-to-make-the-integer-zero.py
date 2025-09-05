class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(36):
            diff = num1 - i*num2
            if diff.bit_count() <= i <= diff:
                return i
        return -1