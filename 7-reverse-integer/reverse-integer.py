class Solution:
    def reverse(self, x: int) -> int:
        multiplier = 1
        num = 0
        if x < 0:
            multiplier = -1
            x = -x
        if x >= (1<<31):
            return 0
        while x >= 1:
            d = x % 10
            num *= 10
            num += d
            x //= 10
        if num >= (1<<31):
            return 0
        return multiplier * int(num)