import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        heap = []
        for l, w in dimensions:
            heappush(heap, (-(l*l + w*w), -l*w))
        return -heap[0][1]