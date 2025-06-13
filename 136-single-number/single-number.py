from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Use reduce to apply XOR operation across all numbers in the array
        # XOR properties:
        # 1. a ^ a = 0 (same number XORed cancels out)
        # 2. a ^ 0 = a (XOR with 0 returns the number)
        # 3. XOR is associative and commutative
        # Thus, all paired numbers cancel out (become 0), leaving the single number
        return reduce(lambda x, y: x ^ y, nums)