class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input array to handle duplicates and enable two-pointer technique
        sorted_nums = sorted(nums)
        # Initialize result list to store valid triplets
        result = []
        # Store length of input array for convenience
        n = len(nums)
        # Iterate through array, using each element as first number (t) of triplet
        for l, t in enumerate(sorted_nums):
            # Skip duplicate values for first number to avoid duplicate triplets
            if l > 0 and sorted_nums[l] == sorted_nums[l-1]:
                continue
            # Initialize right pointer to end of array
            r = n - 1
            # Move left pointer one step beyond current index
            l += 1
            # Use two pointers (l and r) to find two numbers that sum with t to zero
            while l < r:
                # Calculate sum of current triplet
                val = sorted_nums[l] + sorted_nums[r] + t
                # If sum is zero, we found a valid triplet
                if val == 0:
                    # Add triplet to result in sorted order (largest to smallest)
                    result.append([sorted_nums[r], sorted_nums[l], t])
                    # Move left pointer to next different number
                    l += 1
                    # Skip duplicates for left pointer to avoid duplicate triplets
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                # If sum is less than zero, we need a larger sum, so increment left pointer
                elif val < 0:
                    l += 1
                # If sum is greater than zero, we need a smaller sum, so decrement right pointer
                else:
                    r -= 1
        # Return list of all valid triplets
        return result