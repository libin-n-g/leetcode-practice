class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotate(row_start, col_start, n):
            """
            (row_start, col_start) ......(row_start, col_end) 
            ..
            ..
            (row_end, col_start) ......(row_end, col_end)

            (r,c)   -> (r, n-1)     -> (n-1,n-1) -> (n-1, c)
            (r,c+1) -> (r+1, n-1)   -> (n-1,n-2) -> (n-2, c)
            .
            .
            (r, n-2) -> (n-2, n-1) -> (n-1, c+1) -> (r+1, c)
            """
            if n <= 1:
                return 
            row_end = row_start + n - 1
            col_end = col_start + n - 1
            for i, j in zip(range(n-1), range(n-1)):
                # print((row_start, col_start+j), (row_start+i, col_end), (row_end, col_end - j), (row_end-i, col_start))
                matrix[row_start][col_start+j],matrix[row_start+i][col_end],matrix[row_end][col_end - j],matrix[row_end-i][col_start] = matrix[row_end-i][col_start],matrix[row_start][col_start+j],matrix[row_start+i][col_end],matrix[row_end][col_end - j]
            rotate(row_start + 1, col_start + 1, n - 2)
        n = len(matrix)
        rotate(0, 0, n)