class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1, l2 = 0, 1
        n = len(nums)
        while l1 < n:
            while l1 < n-1 and nums[l1] != 0: l1 += 1
            l2 = l1 + 1
            while l2 < n and nums[l2] == 0: l2 += 1
            if l2 < n:
                nums[l1], nums[l2] = nums[l2], nums[l1]
            l1 += 1


        