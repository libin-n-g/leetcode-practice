class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        # for child starting at (0,0)
        best = 0
        for i in range(N):
            best += fruits[i][i]
            fruits[i][i] = float('-inf')
        # for child starting at (0, n-1)
        @cache
        def go_right(x, y):
            if y == N - 1:
                return 0 if x == N - 1 else float('-inf')
            best = float('-inf')
            for dx in range(-1, 2):
                if 0 <= x + dx < N:
                    projected_best = go_right(x + dx, y + 1)
                    if projected_best > best:
                        best = projected_best
            return best + fruits[x][y]
        # for child starting at (n-1, 0)
        @cache
        def go_down(x, y):
            if x == N - 1:
                return 0 if y == N - 1 else float('-inf')
            best = float('-inf')
            for dy in range(-1, 2):
                if 0 <= y + dy < N:
                    projected_best = go_down(x + 1, y + dy)
                    if projected_best > best:
                        best = projected_best
            return best + fruits[x][y]
        ret = best + go_right(N-1, 0) + go_down(0, N-1)
        go_right.cache_clear()
        go_down.cache_clear()
        return ret
            
            