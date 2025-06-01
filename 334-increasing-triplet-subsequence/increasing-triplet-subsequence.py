class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize first and second to infinity
        # first: smallest number seen that could start an increasing triplet
        # second: smallest number seen that could be second in a triplet after some first
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            # Case 1: If num is smaller than or equal to first, update first
            # This ensures first is the smallest possible start of a triplet, maximizing
            # the chance of finding a valid second and third number later
            if num <= first:
                first = num
            # Case 2: If num is larger than first but smaller than or equal to second, update second
            # This means num could be the second number in a triplet, as it's larger than
            # some previous first. Note: second may become less than the current first
            # (e.g., in [20, 100, 10, 12], after seeing 20, 100, 10, we set first=10, second=100,
            # then update second=12, so second=12 < first=10). This is okay because:
            # - second was set when num was greater than an earlier first
            # - A future num > second implies a valid triplet exists (e.g., earlier_first < second < num)
            # - The algorithm doesn't require first and second to be in order in the array at the same time
            # - It tracks potential candidates, ensuring a strictly increasing sequence exists somewhere
            elif num <= second:
                second = num
            # Case 3: If num is larger than both first and second, a triplet is found
            # Since second > some earlier first (when second was set), and num > second,
            # we have earlier_first < second < num, forming a strictly increasing triplet
            # This works even if second < current first, as second relates to a prior first
            else:
                return True
        
        # No increasing triplet found after processing all numbers
        return False