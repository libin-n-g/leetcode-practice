class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_elemets = set(nums)
        if max(nums) <= 0:
            return max(nums)
        else:
            return sum(filter(lambda x: x > 0, unique_elemets))