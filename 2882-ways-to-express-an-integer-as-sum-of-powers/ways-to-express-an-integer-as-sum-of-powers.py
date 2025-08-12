class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        # dp = [0] * (n+1)
        # dp[0] = 1
        # for i in range(n):
        #     if i**x > n:
        #         break
        #     dp[i] = dp() 
        @cache
        def get_ways(n, total, i):
            new_total = total + i**x
            if new_total == n:
                return 1
            if new_total > n:
                return 0
            return (get_ways(n, total, i+1) + get_ways(n, new_total, i+1)) % MOD
        return get_ways(n, 0, 1)
        # xss = set(map(lambda i: i**x, list(range(1, x))))
        # count = 0
        # for xs in xss:
        #     if n - xs in xss:
        #         count += 1

