class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = abs(nums[-1] - nums[0])
        for i in range(1, len(nums)):
            max_diff = max(max_diff, abs(nums[i] -  nums[i-1]))
        return max_diff