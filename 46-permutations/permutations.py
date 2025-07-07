# Generates all possible permutations of the input list using a backtracking approach.
# The algorithm swaps elements to create different orderings, exploring all possibilities
# by recursively fixing one position at a time and swapping subsequent elements.
# Backtracking is achieved by undoing swaps after each recursive exploration.
# Time complexity: O(n*n!), where n is the length of the input list, as it generates all permutations.
# Space complexity: O(n*n!) for storing all permutations, plus O(n) for recursion stack.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []  # Stores all generated permutations
        
        def swap_from_to_end(curr_swap_position):
            # Base case: If we've reached the end of the array, save the current permutation
            if curr_swap_position == len(nums):
                results.append(nums[:])  # Append a copy to avoid modifying the original
                return
            
            # Iterate through each element from current position to end
            for i in range(curr_swap_position, len(nums)):
                # Swap current position with element at index i to create new ordering
                nums[i], nums[curr_swap_position] = nums[curr_swap_position], nums[i]
                
                # Recursively generate permutations for the next position
                swap_from_to_end(curr_swap_position + 1)
                
                # Undo the swap to restore original order for next iteration (backtracking)
                nums[curr_swap_position], nums[i] = nums[i], nums[curr_swap_position]
        
        # Start permutation process from index 0
        swap_from_to_end(0)
        return results

# Example usage:
# Input: nums = [1, 2, 3]
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
# Explanation:
# - Start with [1,2,3].
# - Fix 1, permute [2,3] -> [1,2,3], [1,3,2].
# - Swap 1 with 2, permute [1,3] -> [2,1,3], [2,3,1].
# - Swap 1 with 3, permute [2,1] -> [3,2,1], [3,1,2].
# - Each recursive call explores all possible swaps, building unique permutations.

# Swapping 1 at index 0 with 1 at index 0
# Current array after swap: [1, 2, 3]
# Recursing with position 1
# Swapping 2 at index 1 with 2 at index 1
# Current array after swap: [1, 2, 3]
# Recursing with position 2
# Swapping 3 at index 2 with 3 at index 2
# Current array after swap: [1, 2, 3]
# Recursing with position 3
# Reached end, adding permutation: [1, 2, 3]
# Backtracking, undoing swap: 3 with 3
# Array after backtracking: [1, 2, 3]
# Backtracking, undoing swap: 2 with 2
# Array after backtracking: [1, 2, 3]
# Swapping 2 at index 1 with 3 at index 2
# Current array after swap: [1, 3, 2]
# Recursing with position 2
# Swapping 2 at index 2 with 2 at index 2
# Current array after swap: [1, 3, 2]
# Recursing with position 3
# Reached end, adding permutation: [1, 3, 2]
# Backtracking, undoing swap: 2 with 2
# Array after backtracking: [1, 3, 2]
# Backtracking, undoing swap: 3 with 2
# Array after backtracking: [1, 2, 3]
# Backtracking, undoing swap: 1 with 1
# Array after backtracking: [1, 2, 3]
# Swapping 1 at index 0 with 2 at index 1
# Current array after swap: [2, 1, 3]
# Recursing with position 1
# Swapping 1 at index 1 with 1 at index 1
# Current array after swap: [2, 1, 3]
# Recursing with position 2
# Swapping 3 at index 2 with 3 at index 2
# Current array after swap: [2, 1, 3]
# Recursing with position 3
# Reached end, adding permutation: [2, 1, 3]
# Backtracking, undoing swap: 3 with 3
# Array after backtracking: [2, 1, 3]
# Backtracking, undoing swap: 1 with 1
# Array after backtracking: [2, 1, 3]
# Swapping 1 at index 1 with 3 at index 2
# Current array after swap: [2, 3, 1]
# Recursing with position 2
# Swapping 1 at index 2 with 1 at index 2
# Current array after swap: [2, 3, 1]
# Recursing with position 3
# Reached end, adding permutation: [2, 3, 1]
# Backtracking, undoing swap: 1 with 1
# Array after backtracking: [2, 3, 1]
# Backtracking, undoing swap: 3 with 1
# Array after backtracking: [2, 1, 3]
# Backtracking, undoing swap: 2 with 1
# Array after backtracking: [1, 2, 3]
# Swapping 1 at index 0 with 3 at index 2
# Current array after swap: [3, 2, 1]
# Recursing with position 1
# Swapping 2 at index 1 with 2 at index 1
# Current array after swap: [3, 2, 1]
# Recursing with position 2
# Swapping 1 at index 2 with 1 at index 2
# Current array after swap: [3, 2, 1]
# Recursing with position 3
# Reached end, adding permutation: [3, 2, 1]
# Backtracking, undoing swap: 1 with 1
# Array after backtracking: [3, 2, 1]
# Backtracking, undoing swap: 2 with 2
# Array after backtracking: [3, 2, 1]
# Swapping 2 at index 1 with 1 at index 2
# Current array after swap: [3, 1, 2]
# Recursing with position 2
# Swapping 2 at index 2 with 2 at index 2
# Current array after swap: [3, 1, 2]
# Recursing with position 3
# Reached end, adding permutation: [3, 1, 2]
# Backtracking, undoing swap: 2 with 2
# Array after backtracking: [3, 1, 2]
# Backtracking, undoing swap: 1 with 2
# Array after backtracking: [3, 2, 1]
# Backtracking, undoing swap: 3 with 1
# Array after backtracking: [1, 2, 3]
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]