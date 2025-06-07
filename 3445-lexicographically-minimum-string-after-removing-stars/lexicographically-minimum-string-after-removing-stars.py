class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        min_values = set()
        for i, c in enumerate(s):
            if c == "*":
                _, index = heappop(heap)
                min_values.add(-index)
                min_values.add(i)
                continue
            heappush(heap, (c, -i))
        ret = ""
        for i, c in enumerate(s):
            if i not in min_values:
                ret += c
        return ret

