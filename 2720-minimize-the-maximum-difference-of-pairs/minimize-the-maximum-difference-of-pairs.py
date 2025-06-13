class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Sort the input array to make it easier to find pairs with minimum differences
        sorted_nums = sorted(nums)
        # Get the length of the sorted array
        N = len(sorted_nums)
        
        # Helper function to check if we can form p pairs with max difference <= max_limit
        def check(max_limit):
            i = 1  # Start from index 1 to compare with previous element
            pair_count = 0  # Track number of valid pairs found
            
            # Iterate through array to find p pairs
            while i < N and pair_count < p:
                # Check if difference between adjacent elements is within max_limit
                if sorted_nums[i] - sorted_nums[i-1] > max_limit:
                    i += 1  # Move to next element if difference is too large
                else:
                    i += 2  # Skip both elements of the pair since indices can't be reused
                    pair_count += 1  # Increment pair count
            # Return True if we found exactly p pairs
            return pair_count == p
        
        # Initialize binary search boundaries
        # Left: minimum possible difference (0)
        # Right: maximum possible difference (max - min of array)
        right = sorted_nums[-1] - sorted_nums[0]
        left = 0
        
        # Binary search to find minimum maximum difference
        while left < right:
            mid = left + (right - left) // 2  # Calculate middle point
            if check(mid):
                # If we can form p pairs with this max difference,
                # try a smaller difference
                right = mid
            else:
                # If we can't form p pairs, need a larger difference
                left = mid + 1
        
        # Return the minimum maximum difference
        return left