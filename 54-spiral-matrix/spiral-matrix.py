class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize an empty list to store the spiral order result
        result = []
        # Get the number of rows (m) and columns (n) of the matrix
        m, n = len(matrix), len(matrix[0])
        # Initialize row (i) and column (j) pointers (though only used for initial setup here)
        i = j = 0
        # Continue processing until all elements (m*n) are added to result
        while len(result) < m*n:
            # Process top row: Remove and append the first row to result
            result += matrix.pop(0)

            # Process right column: For each remaining row, remove and append the last element
            for row in matrix:
                if row:  # Check if row is not empty
                    result.append(row.pop())
            
            # Process bottom row: If matrix is not empty, remove and append last row in reverse
            if matrix:
                result += matrix.pop()[::-1]
            
            # Process left column: For each remaining row in reverse order, remove and append first element
            for row in matrix[::-1]:
                if row:  # Check if row is not empty
                    result.append(row.pop(0))
            
        # Return the list containing elements in spiral order
        return result