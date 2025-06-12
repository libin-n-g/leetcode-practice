from itertools import permutations
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        prefixSum_dict = {}
        prefix_length = len(s) + 1
        for i, c in enumerate(s):
            if c not in prefixSum_dict:
                prefixSum_dict[c] = [0]*prefix_length
            for d in prefixSum_dict:
                if c == d:
                    prefixSum_dict[d][i+1] = prefixSum_dict[d][i] + 1
                else:
                    prefixSum_dict[d][i+1] = prefixSum_dict[d][i]
        def calculate_difference(a, b, prefixSum_dict):
            n = len(s)
            min_val = [0, float('inf'), float('inf'), float('inf')]
            min_index = [0, -1, -1, -1]
            max_diff = float('-inf')
            for end in range(k, n+1):
                parityA = prefixSum_dict[a][end] & 1
                parityB = prefixSum_dict[b][end] & 1
                parity = ((parityA ^ 1)  << 1) + parityB
                if min_index[parity] != -1:
                    if prefixSum_dict[b][min_index[parity]] != prefixSum_dict[b][end]:
                        max_diff = max(max_diff, prefixSum_dict[a][end] - prefixSum_dict[b][end] - min_val[parity])

                start = end -k + 1
                parityA = prefixSum_dict[a][start] & 1
                parityB = prefixSum_dict[b][start] & 1
                parity = (parityA << 1) + parityB
                start_diff = prefixSum_dict[a][start] - prefixSum_dict[b][start]
                if start_diff < min_val[parity]:
                    min_val[parity] = start_diff
                    min_index[parity] = start
            return max_diff
        max_diff_result = float('-inf')  
        for a, b in permutations(prefixSum_dict.keys(), 2):
            max_diff_result = max(max_diff_result, calculate_difference(a, b, prefixSum_dict))
        return max_diff_result
