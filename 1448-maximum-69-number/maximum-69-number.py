class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        for i, c in enumerate(digits):
            if c == '6':
                digits[i] = '9'
                break
        return int("".join(digits))