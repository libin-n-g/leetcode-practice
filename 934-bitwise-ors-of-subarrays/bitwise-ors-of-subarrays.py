class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # Initialize an empty set to store unique bitwise OR results
        result = set()
        # Initialize a set to store intermediate bitwise OR results up to index i
        ans_0_i = set()
        
        # Iterate through each number in the input array
        for n in arr:
            # Update ans_0_i by performing bitwise OR of current number n with each
            # existing value in ans_0_i, and include n itself.
            # Example: If ans_0_i = {1, 3} and n = 2, then:
            #   {x | n for x in ans_0_i} = {1 | 2, 3 | 2} = {3, 3} = {3}
            #   {x | n for x in ans_0_i} | {n} = {3} | {2} = {2, 3}
            ans_0_i = {x | n for x in ans_0_i} | {n}
            # Update result set with all intermediate results
            result |= ans_0_i
        
        # Return the count of unique bitwise OR results
        return len(result)