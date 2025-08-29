class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
        given an x, we can have m // 2 choices of y. Hence total choice = n* (m//2)
        """
        return (n*m) // 2