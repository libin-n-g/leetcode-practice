class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        keep = [True] * len(s)
        for i, c in enumerate(s):
            if c == "*":
                _, index = heappop(heap)
                keep[-index] = False
                keep[i] = False
                continue
            heappush(heap, (c, -i))
        ret = ""
        for i, c in enumerate(s):
            if keep[i]:
                ret += c
        return ret

