from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Handle edge case: if amount is 0, no coins are needed
        if amount == 0:
            return 0
        
        # Initialize a queue for BFS to store (remaining_amount, num_coins)
        q = deque([(amount, 0)])
        
        # Initialize visited set to avoid processing the same amount multiple times
        visited = {amount}
        
        # BFS loop to explore all possible coin combinations
        while q:
            # Pop the current amount and number of coins used from the queue
            current_amount, num_coins = q.popleft()
            
            # Try each coin denomination
            for coin in coins:
                # Calculate the new remaining amount after using the current coin
                next_amount = current_amount - coin
                
                # If the remaining amount is 0, we found a valid combination
                if next_amount == 0:
                    return num_coins + 1
                
                # If the remaining amount is positive and not visited, explore it
                if next_amount > 0 and next_amount not in visited:
                    visited.add(next_amount)
                    q.append((next_amount, num_coins + 1))
        
        # If no combination is found, return -1
        return -1