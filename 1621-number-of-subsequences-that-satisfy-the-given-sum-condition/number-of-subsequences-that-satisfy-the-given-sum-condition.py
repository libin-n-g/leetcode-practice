class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        nums.sort()
        left = 0
        right = len(nums) - 1
        ret = 0
        while left <= right:
            while nums[left] + nums[right] > target and left <= right:
                right -= 1
            if left <= right:
                ret += 1 << (right - left)
                # ret = ret % mod
            left += 1
        return ret  % mod