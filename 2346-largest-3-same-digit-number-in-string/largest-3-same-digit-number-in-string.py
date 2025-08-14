class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_number = -1
        count = 0
        counter_char = ""
        for n in num:
            if n == counter_char:
                count += 1
                if count == 3 and max_number < int(counter_char):
                    max_number = int(counter_char)
            else:
                count = 1
                counter_char = n
        
        return str(max_number)*3 if max_number != -1 else ""