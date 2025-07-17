class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # Initialize the maximum length of any valid subsequence
        max_length = 0
        
        # Iterate over all possible target sums of remainders (ik) from 0 to k-1
        # ik represents the desired (a + b) % k for pairs in the subsequence
        for ik in range(k):
            # Create a Counter to store the maximum length of subsequences
            # Key: remainder when a number is divided by k
            # Value: length of the longest subsequence ending with a number having that remainder
            counter = Counter()
            
            # Iterate through each number in the input list
            for num in nums:
                # Calculate the remainder of the current number when divided by k
                reminder = num % k
                
                # Update the counter for this remainder
                # The condition given in question is (a + b) mod k = c 
                # Therefore, a + b = nk + r => a = nk + c - b
                # taking mod on both side, a mod k == (c - b) mod k = ( c mod k - b mod k ) mod k
                # Let r1 = a mod k and r2 = b mod k, then r1 == (c - r2) mod k 
                # (NB: 0 <= c < k becuse it is already reminder)
                # For a number with remainder r, we can extend a subsequence ending with
                # a number having remainder (ik - r) % k, because (r + (ik - r)) % k = ik
                # Thus, counter[reminder] is set to the length of the subsequence ending
                # at (ik - reminder) % k plus 1 (to include the current number)
                counter[reminder] = counter[(ik - reminder) % k] + 1
            
            # Update max_length with the maximum subsequence length for this ik
            # max(counter.values()) gives the longest subsequence ending with any remainder
            max_length = max(max_length, max(counter.values()))
        
        # Return the maximum length found across all possible ik values
        return max_length