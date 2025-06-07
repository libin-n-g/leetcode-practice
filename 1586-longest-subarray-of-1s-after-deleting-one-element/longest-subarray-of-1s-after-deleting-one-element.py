class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_ones, current_ones = 0, 0
        max_length = 0
        for num in nums:
            if num == 1:
                current_ones += 1
                max_length = max(max_length, current_ones + prev_ones) # exclusding zero in between 
            else:
                prev_ones, current_ones = current_ones, 0
        return min(len(nums)-1, max_length) # we must delete one element
        # l = 0 
        # r = 0
        # k = 1
        # max_length = 0
        # while l <= r < len(nums):
        #     while l < r and k <= 0 and nums[r] == 0:
        #         if nums[l] == 0:
        #             k +=1
        #         l += 1
        #     if nums[r] == 0:
        #         k -= 1
        #     if k >= 0:
        #         max_length = max(max_length, r -l)
        #         r += 1
        #     # print(l, r, k, max_length)
        # return max_length


