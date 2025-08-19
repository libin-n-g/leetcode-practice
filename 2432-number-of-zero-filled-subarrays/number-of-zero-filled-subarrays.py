class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        num_zero_arrays = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                left=(right+1)
                continue
            num_zero_arrays += (right - left + 1)
            # print(right, left, num_zero_arrays)
        return num_zero_arrays