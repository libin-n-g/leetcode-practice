class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_number = -1
        counter = Counter(num[0:3])
        if len(counter) == 1:
            max_number = num[0:3]
        for i in range(3, len(num)):
            n = num[i]
            counter[num[i-3]] -= 1
            if counter[num[i-3]] == 0:
                del counter[num[i-3]]
            counter[n] += 1
            if len(counter) == 1 and int(n*3) > int(max_number):
                max_number = n*3

        return max_number if max_number != -1 else ""