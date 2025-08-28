class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            for i_start, j_start in set([(0, i), (i, 0)]):
                digonal = []
                i = i_start
                j = j_start
                while i < n and j < n:
                    digonal.append(grid[i][j])
                    i += 1
                    j += 1
                digonal.sort(reverse=(j_start==0))
                k = 0
                while i > i_start and j > j_start:
                    i -= 1
                    j -= 1
                    grid[i][j] = digonal.pop()
                    k += 1
        return grid