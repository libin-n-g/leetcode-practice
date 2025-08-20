class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ret = sum(matrix[0])
        for i in range(1, m):
            for j in range(0, n):
                if j == 0:
                    ret += matrix[i][j]
                    continue
                elif matrix[i][j] == 0:
                    matrix[i][j] = 0
                    continue
                matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
                ret += matrix[i][j]
        return ret
