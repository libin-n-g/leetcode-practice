class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Initialize left pointer for sliding window
        l = 0
        # Initialize variable to track maximum length of window with ones
        maxsum = 0
        
        # Iterate through array using right pointer (r) and value (num)
        for r, num in enumerate(nums):
            # If we encounter a 0, decrement k (number of allowed flips)
            # For 1s, 1 - num = 0, so k remains unchanged
            k -= 1 - num
            
            # If k becomes negative, we've used more flips than allowed
            if k < 0:
                # Restore k by moving left pointer and accounting for the value at left
                # If nums[l] was 0, this adds 1 back to k; if 1, adds 0
                k += 1 - nums[l]
                # Shrink window by moving left pointer forward
                l += 1
            else:
                # If k >= 0, current window is valid
                # Update maxsum with current window size if larger
                maxsum = max(maxsum, r - l + 1)
        
        # Return the maximum length of consecutive ones found
        return maxsum