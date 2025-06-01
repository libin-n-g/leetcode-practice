class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize a dictionary to store increasing subsequences of different lengths
        # Key 0 maps to an empty list for base case, key 1 starts with the first number
        increasting_subsequeces = {0: [], 1: [nums[0]]}
        # Track the length of the longest increasing subsequence found
        longest_subsequence_length = 1
        # Iterate through each number in the input list
        for num in nums:
            # Check subsequences from longest to shortest
            for i in range(longest_subsequence_length, 0, -1):
                # If current number can extend the subsequence at length i
                if num > increasting_subsequeces[i][-1]:
                    # Create a new subsequence of length i+1 by appending num
                    increasting_subsequeces[i+1] = increasting_subsequeces[i] + [num]
                    # Update the longest subsequence length
                    longest_subsequence_length += 1
                    break
                else:
                    # If num can't extend the current subsequence, try a shorter one
                    # Check if num can extend the subsequence of length i-1
                    if i == 1 or increasting_subsequeces[i-1][-1] < num:
                        # Replace the subsequence at length i with i-1's subsequence plus num
                        increasting_subsequeces[i] = increasting_subsequeces[i-1] + [num]
                        break
            # print(num, increasting_subsequeces)
        # Return the length of the longest increasing subsequence
        return longest_subsequence_length