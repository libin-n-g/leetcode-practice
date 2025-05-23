
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # delta = []
        ret = sum(nums)
        max_negative = float('-inf')
        min_positive = float('inf')
        positive_count = 0
        for i in nums:
            diff = (i ^ k) - i
            # delta.append(diff)
            if diff > 0:
                positive_count += 1
                min_positive = diff if diff < min_positive else min_positive
                ret += diff
            else:
                max_negative = diff if diff > max_negative else max_negative
        if positive_count % 2 == 1:
            return ret - min(-max_negative, min_positive)
        # delta.sort(reverse=True)
        # for i in range(0, len(nums) - 1, 2):
        #     if delta[i] + delta[i+1] > 0:
        #         ret += (delta[i] + delta[i+1])
        return ret