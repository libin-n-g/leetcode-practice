MOD = 10**9 + 7

class Solution:
    def mod_inverse(self, a, m):
        return self.power(a, m-2, m)
    
    def power(self, n, p, m):
        if p == 0:
            return 1
        ans = 1
        n = n % m
        if n == 0:
            return 0
        while p > 0:
            if p & 1:
                ans = (ans * n) % m
            p >>= 1
            n = (n * n) % m
        return ans
    
    def combinations(self, n, r):
        if r > n or r < 0:
            return 0
        # Compute factorials and inverse factorials up to n
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i-1] * i) % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = self.mod_inverse(fact[n], MOD)
        for i in range(n-1, -1, -1):
            inv_fact[i] = (inv_fact[i+1] * (i+1)) % MOD
        return (fact[n] * inv_fact[r] * inv_fact[n-r]) % MOD
    
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if n == 1:
            return m if k == 0 else 0
        if k > n-1 or k < 0:
            return 0
        if m == 1:
            return 1 if k == n-1 else 0
        combinations_of_split = self.combinations(n-1, k)
        possible_assignments = (m * self.power(m-1, n-1-k, MOD)) % MOD
        return (possible_assignments * combinations_of_split) % MOD