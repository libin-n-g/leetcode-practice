MOD = 10**9 + 7
class Solution:
    # def combinations(self, n, r):
    #     ans = 1
    #     for i in range(1, r+1):
    #         ans = (ans * (n-r+i)) % MOD
    #         ans = (ans * self.mod_inverse(i, MOD)) % MOD
    #     return ans

    def factorial(self, n):
        # Compute factorial of n modulo MOD and also return (n-1)! for efficiency
        # Modular factorial ensures large factorials don't overflow by taking modulo at each step
        ans = 1
        prev = 1
        for i in range(1, n+1):
            prev = ans
            ans = (ans * i) % MOD
        return ans, prev

    def get_inverse_factorial_and_factorial(self, n, k):
        # Compute factorial of n and inverse factorials for (n-k)! and k!
        # Inverse factorial is used in combination formula: C(n,k) = n! / (k! * (n-k)!)
        # We use modular inverse to compute division under modulo
        fact_n, fact_n_prev = self.factorial(n)
        result = [fact_n_prev]  # Store (n-1)!
        ans = self.mod_inverse(fact_n, MOD)  # Compute 1/n! mod MOD
        for i in range(n, 0, -1):
            ans = (ans * i) % MOD  # Compute 1/(i-1)! from 1/i! by multiplying by i
            if i == n - k:
                result.append(ans)  # Store 1/(n-k)!
            if i == k + 1:
                result.append(ans)  # Store 1/k!
        return result

    def mod_inverse(self, a, m):
        # Compute modular multiplicative inverse of a under modulo m using Fermat's Little Theorem
        # If m is prime, a^(m-2) mod m is the inverse of a mod m
        return self.power(a, m-2, m)

    def power(self, n, p, m):
        # Compute (n^p) % m efficiently using square-and-multiply algorithm
        ans = 1
        n = n % m
        if n == 0:
            return 0
        while p > 0:
            if p & 0b1 == 1:
                ans = (ans * n) % m
            p = p >> 1  # Divide p by 2
            n = (n * n) % m  # Square n
        return ans

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # Handle base cases
        if k == 0:
            if n == 1:
                return m  # Single element array has m choices
            elif m > 1:
                # First element has m choices, others have m-1 choices (no adjacent same elements)
                return (m * self.power(m-1, n-1, MOD)) % MOD
            else:
                return 0  # If m=1, can't have different adjacent elements for n>1
        if m == 1:
            if k == n-1:
                return 1  # Only one way to arrange n elements with m=1 and k=n-1
            else:
                return 0  # No valid arrangement if k != n-1 when m=1

        # Calculate number of ways to choose k splits (comparisons) from n-1 positions
        # This is equivalent to C(n-1, k) or C(n-1, n-1-k)
        fact_n, inv_fact_n_k, inv_fact_k = self.get_inverse_factorial_and_factorial(n, k)
        # Compute C(n-1, k) = (n-1)! / (k! * (n-1-k)!) using modular arithmetic
        combinations_of_split = (((fact_n * inv_fact_n_k) % MOD) * inv_fact_k) % MOD

        # Calculate possible assignments of values
        # First segment has m choices, subsequent segments have m-1 choices
        possible_assignments = (m * self.power(m-1, n-k-1, MOD)) % MOD

        # Total ways = number of splits * number of valid assignments
        return (possible_assignments * combinations_of_split) % MOD
            
        