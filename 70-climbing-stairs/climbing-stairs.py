class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        mem_1, mem_2 = 1, 2
        for i in range(2, n):
            mem_1, mem_2 = mem_2, mem_1 + mem_2
        return mem_2
        