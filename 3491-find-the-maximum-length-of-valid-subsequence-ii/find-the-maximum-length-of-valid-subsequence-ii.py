class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        max_length = 0
        for ik in range(k):
            counter = Counter()
            for num in nums:
                reminder = num % k
                counter[reminder] = counter[(ik - reminder) % k] + 1
            max_length = max(max_length, max(counter.values()))
            # print(counter)
        return max_length