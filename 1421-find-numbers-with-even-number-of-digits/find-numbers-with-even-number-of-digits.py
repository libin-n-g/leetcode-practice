class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            for r in [10, 1000, 100000]:
                if r <= num < 10*r:
                    ret += 1
                    break
        return ret
    # def findNumbers(self, nums: List[int]) -> int:
    #     count = 0
    #     n = len(nums)
    #     for j in range(n): 
    #         num = nums[j]
    #         num_digits = 0
    #         while num >= 1:
    #             num = num / 10
    #             num_digits += 1
    #             # print(num, num_digits)
    #             if num < 1 and num_digits % 2 == 0:
    #                 count += 1
    #                 break
    #     return count


