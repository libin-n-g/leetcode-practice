class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        min_values = set()
        for i, c in enumerate(s):
            if c == "*":
                # prev_c, last_min = stack[-1]
                # if 
                char, index = heappop(heap)
                min_values.add(-index)
                continue
            heappush(heap, (c, -i))
            # min_value = min(min_value, c)
            # stack.append((c, min_value))
        print(min_values)
        ret = ""
        for i, c in enumerate(s):
            if i not in min_values and c != "*":
                ret += c
        return ret

