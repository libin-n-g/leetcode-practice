class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        sorted_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        ret = 0
        while left <= right:
            if sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            else:
                ret = (ret + 2**(right - left)) % mod
                left += 1
        return ret