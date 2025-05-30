class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (n*(n+1) - 2*m*(n//m)*(n//m + 1))//2
        # ret = 0
        # for i in range(1, n+1):
        #     if i % m == 0:
        #         ret -= i
        #     else:
        #         ret += i
        # return ret