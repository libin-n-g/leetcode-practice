class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_value = 0
        max_count = 0
        counts = Counter()
        for right in range(len(s)):
            counts[s[right]] += 1
            max_count = max(max_count, counts[s[right]])
            while right - left + 1 - max_count > k:
                counts[s[left]]  -= 1
                left += 1
            max_value = max(right -left + 1, max_value)
        return max_value
