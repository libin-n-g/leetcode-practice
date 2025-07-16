class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        length = Counter()
        for num in nums:
            if num % 2 == 0:
                length[2] += 1
                length[12] = length[21] + 1
            else:
                length[1] += 1
                length[21] = length[12] + 1
        return max(length.values())
                    