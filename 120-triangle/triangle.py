class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def get_mininum_total(level, index):
            if level + 1 < n:
                return triangle[level][index] + \
                min(get_mininum_total(level + 1, index), get_mininum_total(level + 1, index + 1))
            return triangle[level][index]
        get_mininum_total.cache_clear()
        return get_mininum_total(0, 0)