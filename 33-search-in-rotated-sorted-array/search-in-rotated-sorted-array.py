class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers: left at start, right at end of array
        left = 0
        right = len(nums) - 1
        
        # Continue searching while left pointer doesn't exceed right pointer
        while left <= right:
            # Calculate middle index using safe method to avoid integer overflow
            mid = left + (right - left) // 2
            
            # If target is found at mid, return the index
            if nums[mid] == target:
                return mid
                
            # Check if right half is sorted (nums[mid] < nums[right])
            if nums[mid] < nums[right]:
                # Right half is sorted
                # Check if target lies within the sorted right half range
                if nums[mid] < target <= nums[right]:
                    # Target is in the right half
                    left = mid + 1
                else:
                    # Target is in the left half
                    right = mid - 1
            else:
                # Left half is sorted (since right half is not)
                # Check if target lies within the sorted left half range
                if nums[left] <= target < nums[mid]:
                    # Target is in the left half
                    right = mid - 1
                else:
                    # Target is in the right half
                    left = mid + 1
                    
        # Target not found in array
        return -1