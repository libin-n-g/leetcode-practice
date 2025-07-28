class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda x, y : x | y, nums)
        N = len(nums)
        results = 0
        # def count_subsets(subsets=[], index=0, prev_xor=0):
        #     result = 0
        #     if prev_xor == max_or:
        #         result += 1
        #     for i in range(index, N):
        #         subsets.append(nums[i])
        #         result += find_subsets(subsets, i+1, prev_xor | nums[i])
        #         subsets.pop()
        #     return result
        def count_subsets(index, current_or):
            if index == N:
                return 1 if current_or == max_or else 0
            count_with_i = count_subsets(index + 1, current_or | nums[index])
            count_without_i = count_subsets(index + 1, current_or)
            return count_with_i + count_without_i
        return count_subsets(0, 0)