class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        current_power = 1
        while n > 0:
            if n & 0b1:
                powers.append(current_power)
            n = n >> 1
            current_power = current_power << 1
        prefix_product = [1] * (len(powers)+1)
        prefix_product[0] = powers[0]
        for i, p in enumerate(powers):
            prefix_product[i+1] = prefix_product[i]*p
        ret = []
        for s, e in queries:
            r = prefix_product[e+1]//prefix_product[s]
            ret.append(r % MOD)
        return ret
            