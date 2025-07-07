class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # BACKTRACKING
        # results = []
        # def backtrack(subset=[], item_index=0):
        #     results.append(subset[:]) # shallow copy

        #     for i in range(item_index, len(nums)):
        #         subset.append(nums[i])
        #         backtrack(subset, i + 1)
        #         subset.pop()
        # backtrack()
        # return results
        results = [[]]
        for item in nums:
            for i in range(len(results)):
                subset = results[i]
                results.append(subset + [item])
        return results