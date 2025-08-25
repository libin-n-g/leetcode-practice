class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        0,0 
        0, 1 -> 1, 0
        2, 0 -> 1, 1 -> 0, 2
        1, 2 -> 2, 1
        2, 2
        """
        ret = []
        m , n = len(mat), len(mat[0])
        for sum_val in range(m+n):
            row = []
            for i in range(m):
                j = sum_val - i
                if 0 <= j < n:
                    row.append(mat[i][j])
            if sum_val % 2 == 0:
                row = row[::-1]
            ret.extend(row)
        return ret
