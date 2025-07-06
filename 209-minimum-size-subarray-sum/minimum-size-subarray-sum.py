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

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize prefix sum array with one extra element for easier calculation
        prefix_sum = [0]*(len(nums)+1)
        prefix_sum[0] = 0  # Set first element to 0 for base case
        n = len(nums)      # Store length of input array
        ret = n + 1        # Initialize result to length of array + 1 (impossible length)

        # Calculate prefix sums: prefix_sum[i+1] stores sum of nums[0:i]
        for i, num in enumerate(nums):
            prefix_sum[i+1] = prefix_sum[i] + num 

        # If total sum is less than target, no valid subarray exists
        if prefix_sum[n] < target:
            return 0

        # Iterate through each possible starting index
        for i in range(len(nums)):
            l = i          # Left pointer starts at current index
            r = n - 1      # Right pointer starts at end of array
            # Binary search to find smallest subarray starting at i
            while l <= r:
                mid = l + (r - l)//2  # Calculate middle index
                # Check if subarray sum from i to mid is >= target
                if prefix_sum[mid + 1] - prefix_sum[i] >= target:
                    # If target sum is achieved, update minimum length and search left half
                    ret = min(ret, mid - i + 1)
                    r = mid - 1
                else:
                    # If sum is too small, search right half
                    l = mid + 1

        # Return minimum length found (or n+1 if no valid subarray)
        return ret

