class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # This function finds the smallest n such that num1 - n*num2 can be expressed as a sum of n distinct powers of 2.
        # For example, if num1 = 12 and num2 = 1, then for n = 2: 12 - 2*1 = 10. Since 10 = 2^3 + 2^1 (binary 1010, two 1's),
        # and bit_count(10) = 2 <= n = 2 <= diff = 10, n = 2 is a valid solution. The function checks if the number of 1's
        # in the binary representation of num1 - n*num2 is at most n, and n is at most the difference, ensuring the difference
        # can be represented as a sum of n powers of 2.
        # 2^x can be divided into two 2^(x-1) + 2^(x-1). repeating this we can create any n between both.
        for i in range(36):
            diff = num1 - i*num2
            if diff.bit_count() <= i <= diff:
                return i
        return -1