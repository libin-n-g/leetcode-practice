class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the list with the first number to track the longest increasing subsequence
        longest_subsequence = [nums[0]]
        # Iterate through the remaining numbers in the input list
        for num in nums[1:]:
            # If the current number is greater than the last number in the subsequence
            if longest_subsequence[-1] < num:
                # Append the number to extend the increasing subsequence
                longest_subsequence.append(num)
                continue
            # If the number cannot extend the subsequence, find the smallest number
            # in the subsequence that is greater than or equal to the current number
            for i, sub_sequence_endding in enumerate(longest_subsequence):
                if sub_sequence_endding >= num:
                    # Replace the smallest number >= num to maintain a potential
                    # for a longer increasing subsequence
                    longest_subsequence[i] = num
                    break
        # Return the length of the longest increasing subsequence
        return len(longest_subsequence)
    
    
    def lengthOfLIS_trial1(self, nums: List[int]) -> int:
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