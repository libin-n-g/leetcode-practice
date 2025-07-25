class Solution:
    def climbStairs(self, n: int) -> int:
        # mem = [n+1]*(n)
        # mem[0] = 1 # step 1
        # if n > 1:
        #     mem[1] = 2 # step 2
        # for i in range(2, n):
        #     mem[i] = mem[ i - 1] + mem[i - 2]
        # return mem[n-1]
        if n == 1:
            return 1
        mem_1, mem_2 = 1, 2
        for i in range(2, n):
            mem_1, mem_2 = mem_2, mem_1 + mem_2
        return mem_2
        