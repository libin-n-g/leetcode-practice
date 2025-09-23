class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        reverse_map = defaultdict(int)
        max_freq = 1
        for k, v in c.items():
            reverse_map[v] += v
            max_freq = max(v, max_freq)
        return reverse_map[max_freq]