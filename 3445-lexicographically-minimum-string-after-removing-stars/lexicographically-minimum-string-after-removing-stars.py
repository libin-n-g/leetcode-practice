class Solution:
    def clearStars(self, s: str) -> str:
        stacks = [[] for _ in range(26)]
        keep = [True] * len(s)
        for i, c in enumerate(s):
            if c == "*":
                keep[i] = False
                j = 0
                while j < 26:
                    if stacks[j]:
                        keep[stacks[j].pop()] = False
                        break
                    j += 1
                continue
            stacks[ord(c) - ord('a')].append(i)
        ret = ""
        for i, c in enumerate(s):
            if keep[i]:
                ret += c
        return ret

