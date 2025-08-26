class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        max_x = max_y =  0
        min_y = min_x = 1001
        # O(n^2)
        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val:
                    max_x = max(x, max_x)
                    max_y = max(y, max_y)
                    min_x = min(x, min_x)
                    min_y = min(y, min_y)
        # for x in range(len(grid)):
        #     if any(grid[x]):
        #         min_x = x
        #         break
        # for x in range(len(grid)-1, -1, -1):
        #     if any(grid[x]):
        #         max_x = x
        #         break
        # for y in range(len(grid[0])):
        #     if any(row[y] for row in grid):
        #         min_y = y
        #         break
        # for y in range(len(grid[0])-1, -1, -1):
        #     if any(row[y] for row in grid):
        #         max_y = y
        #         break
        return (max_x - min_x + 1)*(max_y - min_y + 1)
                
