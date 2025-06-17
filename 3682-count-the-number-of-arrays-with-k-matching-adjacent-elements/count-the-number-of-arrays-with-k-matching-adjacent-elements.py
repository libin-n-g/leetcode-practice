MOD = 10**9 + 7
class Solution:
    # def combinations(self, n, r):
    #     ans = 1
    #     for i in range(1, r+1):
    #         ans = (ans * (n-r+i)) % MOD
    #         ans = (ans * self.mod_inverse(i, MOD)) % MOD
    #     return ans

    def factorial(self, n):
        ans = 1
        prev = 1
        for i in range(1, n+1):
            prev = ans
            ans=(ans * i) % MOD
        return ans, prev
    def get_inverse_factorial_and_factorial(self, n, k):
        fact_n, fact_n_prev = self.factorial(n)
        result = [fact_n_prev]
        ans = self.mod_inverse(fact_n, MOD)
        for i in range(n, 0, -1):
            ans = (ans*i) % MOD
            if i == n - k:
                result.append(ans)
            if  i == k + 1:
                result.append(ans)
        return result

    def mod_inverse(self, a, m):
        return self.power(a, m-2, m)
    
    def power(self, n, p, m):
        ans = 1
        n = n % m
        if n == 0:
            return 0
        while p > 0:
            if p & 0b1 == 1:
                ans = (ans * n) % m
            p = p >> 1 # y // 2
            n = (n*n) % m
        return ans
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            if n == 1:
                return m
            elif m > 1:
                return m*((m-1)**(n-1)) % MOD
            else:
                return 0
        if m == 1:
            if k == n-1:
                return 1
            else:
                return 0
        # consider aaaabbbbcccc
        # if we have n char then we need to compare n-1 times. 
        # so choose k split(comparisons) from n-1 or (n-1)C(k) or (n-1)C(n-1-k)
        fact_n, inv_fact_n_k, inv_fact_k  = self.get_inverse_factorial_and_factorial(n, k)
        print(fact_n, inv_fact_n_k, inv_fact_k)
        combinations_of_split = (((fact_n * inv_fact_n_k) % MOD) * inv_fact_k)  % MOD
        # If first aa has m posiblities then bbb.. has m-1 possiblities abd cc.. has m-1 possibities etc. 
        possible_assignments = (m * self.power(m-1, n-k-1, MOD)) % MOD
        return possible_assignments*combinations_of_split % MOD
            
        