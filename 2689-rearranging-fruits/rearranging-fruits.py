class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Create a Counter to track the frequency of items in basket1
        counter = Counter(basket1)
        # Find the minimum value across both baskets to use as a potential swap cost
        min_value = min(min(basket1), min(basket2))
        
        # Subtract the frequency of items in basket2 from the counter
        # This gives us the net difference in item counts between baskets
        for item in basket2:
            counter[item] -= 1
        
        # Initialize an array to store items that need to be transferred
        trasfer_array = []
        for item, freq in counter.items():
            # If the frequency is odd, baskets cannot be made equal
            if freq % 2 == 1:
                return -1
            # Add each item abs(freq)//2 times to the transfer array
            # This represents the number of items to move to balance the baskets
            trasfer_array.extend([item] * (abs(freq) // 2))
        
        # Sort the transfer array to process smallest items first
        trasfer_array.sort()
        
        # Calculate the minimum cost by taking the smaller of:
        # - The item value itself (direct swap cost)
        # - Twice the minimum value in either basket (representing a strategic 3-way swap). [6, 1, 6] and [5, 5, 1] 5 and 6 can be swapped by swapping 5 and 1 then 6 and 1. 
        # Only process the first half of the transfer array since we need equal swaps
        cost = 0
        for i in trasfer_array[:len(trasfer_array)//2]:
            cost += min(2*min_value, i)
        
        return cost