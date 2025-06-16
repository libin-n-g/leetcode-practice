class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1
        for i in range(n):
            for j in range(i+1, n):
                new_diff = nums[j] - nums[i]
                if new_diff > 0:
                    max_diff = max(max_diff, nums[j] - nums[i])
        return max_diff