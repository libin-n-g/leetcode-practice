class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_number = -1
        for i in range(3, len(num)+1):
            n = num[i-3:i]
            if len(Counter(n)) == 1 and int(n) > int(max_number):
                max_number = n
        return max_number if max_number != -1 else ""