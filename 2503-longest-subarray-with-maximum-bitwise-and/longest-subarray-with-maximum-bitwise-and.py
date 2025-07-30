class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = max(nums)
        length = max_length = 0
        for n in nums:
            if n == max_value:
                length += 1
                max_length = max(length, max_length)
            else:
                length = 0
        return max_length