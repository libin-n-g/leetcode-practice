class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        increasting_subsequeces = {0: [], 1: [nums[0]]}
        longest_subsequence_length = 1
        for num in nums:
            for i in range(longest_subsequence_length, 0, -1):
                if num > increasting_subsequeces[i][-1]:
                    increasting_subsequeces[i+1] = increasting_subsequeces[i] + [num]
                    longest_subsequence_length += 1
                    break
                    # if i+1 in increasting_subsequeces:
                    #     increasting_subsequeces[i+1] = increasting_subsequeces[i] + [num]
                    # else:
                else:
                    if i == 1 or increasting_subsequeces[i-1][-1] < num:
                        increasting_subsequeces[i] = increasting_subsequeces[i-1] + [num]
                        break
            # print(num, increasting_subsequeces)
        return longest_subsequence_length
