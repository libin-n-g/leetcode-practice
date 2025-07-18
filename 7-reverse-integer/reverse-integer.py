class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        multiplier = 1
        if x < 0:
            multiplier = -1
            x = -x
        print((1<<31))
        if x >= (1<<31):
            return 0
        while x >= 1:
            digits.append(x % 10)
            x //= 10
        num = 0
        for d in digits:
            num *= 10
            num += d
        if num >= (1<<31):
            return 0
        return multiplier * int(num)