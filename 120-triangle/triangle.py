class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     # Get the number of rows in the triangle
    #     n = len(triangle)
        
    #     @cache  # Memoize the recursive function to avoid redundant calculations
    #     def get_mininum_total(level, index):
    #         # Base case: if at the last row, return the value at the current index
    #         if level + 1 < n:
    #             # Recursive case: add current value to the minimum of the two possible paths below
    #             return triangle[level][index] + \
    #                    min(get_mininum_total(level + 1, index), get_mininum_total(level + 1, index + 1))
    #         return triangle[level][index]
    #     ret = get_mininum_total(0, 0)
    #     get_mininum_total.cache_clear()
    #     return ret

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle[-1])
        dp = triangle[-1][:]
        for level in range(n-2, -1, -1):
            for i in range(level+1):
                dp[i] = min(dp[i],dp[i+1]) + triangle[level][i]
        return dp[0]