class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda x, y : x | y, nums)
        N = len(nums)
        results = 0
        def find_subsets(subsets=[], index=0, prev_xor=0):
            result = 0
            if prev_xor == max_or:
                result += 1
            for i in range(index, N):
                subsets.append(nums[i])
                result += find_subsets(subsets, i+1, prev_xor | nums[i])
                subsets.pop()
            return result
        return find_subsets()