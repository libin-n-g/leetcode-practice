class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize return value as array length (maximum possible subarray length)
        ret = len(nums)
        # Left pointer for sliding window
        l = 0
        # Running sum of current window
        total = 0
        # Iterate through array with right pointer
        for r, n in enumerate(nums):
            # Add current number to running sum
            total += n
            # While window sum meets or exceeds target, try to minimize window
            while total >= target:
                # Update minimum length if current window is smaller
                ret = min(ret, r - l + 1)
                # Shrink window from left by subtracting leftmost number
                total -= nums[l]
                # Move left pointer rightward
                l += 1
        # If left pointer never moved and sum is less than target, no valid subarray exists
        if l == 0 and total < target:
            return 0
        # Return minimum subarray length found
        return ret