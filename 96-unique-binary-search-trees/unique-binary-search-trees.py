class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        def get_num_trees(n):
            if n in dp:
                return dp[n]
            num = 0
            for i in range(n):
                num += get_num_trees(i) * get_num_trees(n-i-1)
            dp[n] = num
            return num
        return get_num_trees(n)