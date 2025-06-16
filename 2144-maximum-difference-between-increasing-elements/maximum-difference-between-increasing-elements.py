class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1
        max_element_till_now = nums[n-1]
        for i in range(n-2, -1, -1):
            if max_element_till_now <= nums[i]:
                max_element_till_now = nums[i]
            else:
                max_diff = max(max_diff, max_element_till_now - nums[i])
        return max_diff