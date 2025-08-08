class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = [1 for i in range(len(nums))]
        down = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] > nums[i]:
                    down[i] = max(down[i], up[j] + 1)
                if nums[j] < nums[i]:
                    up[i] = max(up[i], down[j] + 1)
        return max(max(up), max(down))