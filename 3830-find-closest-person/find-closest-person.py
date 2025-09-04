class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1 = abs(z-y)
        d2 = abs(z-x)
        if d1 == d2:
            return 0
        elif d1 < d2:
            return 2
        return 1