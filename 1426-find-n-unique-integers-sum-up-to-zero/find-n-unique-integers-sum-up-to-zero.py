class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = [0] if n % 2 == 1 else []
        for i in range(n//2):
            ret.append(i+1)
            ret.append(-i-1)
        return ret