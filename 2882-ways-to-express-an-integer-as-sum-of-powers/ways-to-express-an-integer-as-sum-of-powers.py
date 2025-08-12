class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            power =  i**x 
            if power > n:
                break
            for j in range(n, power - 1, -1):
                dp[j] = (dp[j] + dp[j - power]) % MOD
            # print(dp)
        return dp[-1]
        # @cache
        # def get_ways(n, total, i):
        #     new_total = total + i**x
        #     if new_total == n:
        #         return 1
        #     if new_total > n:
        #         return 0
        #     return (get_ways(n, total, i+1) + get_ways(n, new_total, i+1)) % MOD
        # return get_ways(n, 0, 1)
        

