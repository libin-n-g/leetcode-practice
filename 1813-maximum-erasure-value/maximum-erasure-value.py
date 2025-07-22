class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        seen = set()
        right = 0
        score = 0
        max_score = 0
        while left <= right < len(nums):
            if nums[right] in seen:
                seen.remove(nums[left])
                score -= nums[left]
                left += 1
            else:
                seen.add(nums[right])
                score += nums[right]
                right += 1
            max_score = max(score, max_score)
        return max_score
