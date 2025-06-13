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
                # Check if target is less than middle element
                if target < nums[mid]:
                    # Target is less than middle, must be in left half
                    right = mid - 1
                # Check if target is greater than rightmost element
                elif target > nums[right]:
                    # Target is larger than largest element in sorted right half
                    # Must be in left half
                    right = mid - 1
                else:
                    # Target is within the sorted right half range
                    # Search right half
                    left = mid + 1
            else:
                # Left half is sorted (since right half is not)
                # Check if target is greater than middle element
                if target > nums[mid]:
                    # Target is larger than middle, must be in right half
                    left = mid + 1
                # Check if target is less than leftmost element
                elif target < nums[left]:
                    # Target is smaller than smallest element in sorted left half
                    # Must be in right half
                    left = mid + 1
                else:
                    # Target is within the sorted left half range
                    # Search left half
                    right = mid - 1
                    
        # Target not found in array
        return -1