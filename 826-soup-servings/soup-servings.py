class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        @cache
        def calc(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            return (calc(a - 100, b) + calc(a - 75, b - 25) + calc(a - 50, b - 50) + calc(a - 25, b - 75))/4
        return calc(n, n)
            
        