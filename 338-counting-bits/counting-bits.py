class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize result array of size n+1 with zeros
        # mem[i] will store the number of 1's in binary representation of i
        mem = [0] * (n + 1)
        
        # Initialize offset to track the most recent power of 2
        # Used to relate current number to a previous number
        offset = 1
        
        # Iterate through numbers from 1 to n
        for i in range(1, n + 1):
            # Check if i is a power of 2 (i.e., i == 2^k)
            # If true, update offset to current i
            if offset * 2 == i:
                offset = i
            
            # Number of 1's in i is equal to number of 1's in (i - offset) plus 1
            # Because i can be represented as (i - offset) + offset, where offset is a power of 2
            mem[i] = mem[i - offset] + 1
        
        # Return the array containing count of 1's for each number from 0 to n
        return mem