class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        current_num = int(number)
        max_number = 0
        for i, num in enumerate(number):
            if num == digit:
                new_number = number[:i] + number[i+1:]
                if max_number < int(new_number):
                    max_number = int(new_number)
        return str(max_number)