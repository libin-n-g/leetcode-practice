class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        max_freq, min_freq = 0, 101
        for key in counter:
            if counter[key] % 2 == 0:
                min_freq = min(min_freq, counter[key])
            else:
                max_freq = max(max_freq, counter[key])
        return max_freq - min_freq