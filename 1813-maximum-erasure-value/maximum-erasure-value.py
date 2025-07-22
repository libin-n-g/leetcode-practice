class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        seen = set()
        right = 0
        score = 0
        N = len(nums)
        max_score = 0
        for right in range(N):
            while nums[right] in seen:
                seen.remove(nums[left])
                score -= nums[left]
                left += 1
            seen.add(nums[right])
            score += nums[right]
            max_score = max(score, max_score)
        return max_score
