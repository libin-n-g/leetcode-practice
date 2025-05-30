class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1]*n
        ret[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            ret[i] = ret[i+1] * nums[i] 
        for i in range(n):
            if 0 < i < n - 1:
                nums[i] *= nums[i-1]
                ret[i] = ret[i+1] * nums[i-1]
            elif i == n-1:
                nums[i] *= nums[i-1]
                ret[i] = nums[i-1]
            else:
                ret[i] = ret[i+1]
        return ret