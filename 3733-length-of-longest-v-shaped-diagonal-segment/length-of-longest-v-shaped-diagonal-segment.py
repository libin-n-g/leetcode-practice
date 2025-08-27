class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        next_val = {
            1: 2,
            2: 0,
            0: 2,
        }
        @cache
        def dfs(x, y, prev_dir, turned):
            # path.append((x,y))
            max_depth = 1
            prev_value = grid[x][y]
            new_x = x + prev_dir[0]
            new_y = y + prev_dir[1]
            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == next_val[prev_value]:
                max_depth = 1 + dfs(new_x, new_y, prev_dir, turned)
            if not turned:
                dx, dy = prev_dir[1], -prev_dir[0]
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < m and 0 <= new_y < n:
                    if grid[new_x][new_y] == next_val[prev_value]:
                        max_depth = max(max_depth, dfs(new_x, new_y, (dx, dy), True) + 1)
            return max_depth
        ret = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
                        ret = max(ret, dfs(i, j, (dx,dy), False))
        dfs.cache_clear()
        return ret