class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        maxsum = 0
        while r < len(nums):
            while r < len(nums) and k >= 0: 
                if nums[r] == 0:
                    k-=1
                r+=1
                if k >= 0:
                    maxsum = max(maxsum, r - l)
            while l < len(nums) and k < 0:
                if nums[l] == 0:
                    k+=1
                l+=1
                if k >= 0:
                    maxsum = max(maxsum, r - l)
        return maxsum