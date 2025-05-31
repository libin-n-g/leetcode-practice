class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 1
        ret = []
        # Ret is used to store prefix sum except the last element. 
        # note that 1 is added in the begining
        # ret[i] represents product of every element before it (exclusing ith element)
        for num in nums:
            ret.append(p)
            p *= num
        p = 1
        # Suffix sum. Starts with p == 1 and p value is used from previous iteration. 
        # This p value will be product of all elements after i index element. 
        # The p calcullated in i index of loop is product of all elements after index i (including i)
        for i in range(n-1, -1, -1):
            ret[i] = ret[i] * p
            p *= nums[i]
        return ret