class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(1, numRows):
            newRow = [1]*(i+1)
            for j in range(1, i):
                newRow[j] = result[-1][j-1] + result[-1][j]
            result.append(newRow)
        return result