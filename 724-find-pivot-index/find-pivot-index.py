class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = [0]*(len(nums)+2)
        for i, num in enumerate(nums):
            prefix_sums[i+1] = prefix_sums[i] + num
        prefix_sums[-1] = prefix_sums[-2]
        ret = -1
        for i in range(len(nums)):
            if prefix_sums[i] - prefix_sums[0] == prefix_sums[-1] - prefix_sums[i+1]:
                return i
        return -1