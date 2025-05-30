class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 1
        ret = []
        for num in nums:
            ret.append(p)
            p *= num
        p = 1
        for i in range(n-1, -1, -1):
            ret[i] = ret[i] * p
            p *= nums[i]
        return ret