class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Initialize result array with same length as input array
        result = [0] * len(nums)
        # Two pointers: l points to start, r points to end of input array
        l, r = 0, len(nums) - 1
        # Iterate backwards through result array (from largest to smallest index)
        for i in range(len(nums) - 1, -1, -1):
            # Compare absolute values of numbers at left and right pointers
            if abs(nums[l]) > abs(nums[r]):
                # If left number's absolute value is larger, square it and place at current index
                result[i] = nums[l] * nums[l]
                # Move left pointer rightward
                l += 1
            else:
                # If right number's absolute value is larger or equal, square it and place at current index
                result[i] = nums[r] * nums[r]
                # Move right pointer leftward
                r -= 1
        # Return sorted array of squared numbers
        return result