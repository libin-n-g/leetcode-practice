class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        count = 0
        for x in range(1, n+1):
            if x % 2 == 0:
                count += (m+1) // 2
            else:
                count += m // 2
        return count