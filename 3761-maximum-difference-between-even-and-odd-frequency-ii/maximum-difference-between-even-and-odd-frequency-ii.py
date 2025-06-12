from itertools import permutations

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # Initialize a dictionary to store prefix sums for each character in the string
        prefixSum_dict = {}
        # Length of prefix sum arrays (string length + 1 for 0-based indexing)
        prefix_length = len(s) + 1
        
        # Build prefix sum arrays for each unique character in the string
        for i, c in enumerate(s):
            # If character c is not in the dictionary, initialize its prefix sum array
            if c not in prefixSum_dict:
                prefixSum_dict[c] = [0] * prefix_length
            # Update prefix sums for all characters
            for d in prefixSum_dict:
                if c == d:
                    # If current character matches, increment the prefix sum
                    prefixSum_dict[d][i + 1] = prefixSum_dict[d][i] + 1
                else:
                    # Otherwise, copy the previous prefix sum
                    prefixSum_dict[d][i + 1] = prefixSum_dict[d][i]

        # Helper function to calculate max difference for a pair of characters (a, b)
        def calculate_difference(a, b, prefixSum_dict):
            n = len(s)
            # min_val stores minimum differences for each parity combination
            # Format: [evenA/evenB, evenA/oddB, oddA/evenB, oddA/oddB]
            min_val = [0, float('inf'), float('inf'), float('inf')]
            # min_index stores the index where minimum difference occurs for each parity
            min_index = [0, -1, -1, -1]
            # Initialize max difference as negative infinity
            max_diff = float('-inf')
            
            # Iterate over all possible end indices for substrings of length >= k
            for end in range(k, n + 1):
                # Calculate parities of prefix sums for characters a and b at end index
                parityA = prefixSum_dict[a][end] & 1  # 0 if even, 1 if odd
                parityB = prefixSum_dict[b][end] & 1  # 0 if even, 1 if odd
                # Compute parity index: ((parityA ^ 1) << 1) + parityB
                # Maps to: evenA/evenB: 0, evenA/oddB: 1, oddA/evenB: 2, oddA/oddB: 3
                # The XOR (^ 1) inverts parityA because we need freq[a] - freq[b] where a has odd frequency
                # and b has even frequency in the substring. This maps transitions like:
                # evenA/evenB (00) -> oddA/evenB (10), evenA/oddB (01) -> oddA/oddB (11), etc.
                parity = ((parityA ^ 1) << 1) + parityB
                
                # If a minimum difference exists for this parity combination
                if min_index[parity] != -1:
                    # Check if count of b differs between current end and min_index
                    # Ensures the substring is valid (non-zero length)
                    if prefixSum_dict[b][min_index[parity]] != prefixSum_dict[b][end]:
                        # Update max_diff if current difference is larger
                        # Difference = (count[a] at end - count[b] at end) - min(count[a] - count[b])
                        max_diff = max(max_diff, prefixSum_dict[a][end] - prefixSum_dict[b][end] - min_val[parity])
                
                # Calculate start index for substring of length k
                start = end - k + 1
                # Calculate parities at start index
                parityA = prefixSum_dict[a][start] & 1
                parityB = prefixSum_dict[b][start] & 1
                # Compute parity index for start: evenA/evenB: 0, oddA/evenB: 2, etc.
                # No XOR here, as we store the actual parities at the start index
                parity = (parityA << 1) + parityB
                # Calculate difference at start index
                start_diff = prefixSum_dict[a][start] - prefixSum_dict[b][start]
                # Update minimum difference and index for this parity if smaller
                if start_diff < min_val[parity]:
                    min_val[parity] = start_diff
                    min_index[parity] = start
            
            return max_diff

        # Initialize result as negative infinity
        max_diff_result = float('-inf')
        # Iterate over all pairs of distinct characters
        for a, b in permutations(prefixSum_dict.keys(), 2):
            # Update result with maximum difference for each character pair
            max_diff_result = max(max_diff_result, calculate_difference(a, b, prefixSum_dict))
        
        return max_diff_result