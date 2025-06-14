class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num % 10)
            num = num // 10
        print(digits)
        min_replacement_digit = None
        max_replacement_digit = None
        for d in digits[::-1]:
            if d != 9 and max_replacement_digit is None:
                max_replacement_digit = d
            if d != 0 and min_replacement_digit is None:
                min_replacement_digit = d
            if min_replacement_digit and max_replacement_digit:
                break
        diff = 0
        for p, d in enumerate(digits):
            if d == max_replacement_digit == min_replacement_digit:
                current_digit = 9 
            elif d == max_replacement_digit:
                current_digit = 9 - d
            elif d == min_replacement_digit:
                current_digit = d 
            else: 
                current_digit = 0
            diff += (current_digit*10**p)
        return diff

