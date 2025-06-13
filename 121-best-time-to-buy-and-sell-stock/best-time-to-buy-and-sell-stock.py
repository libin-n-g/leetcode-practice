class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize buy_day to track the day with lowest price seen so far
        buy_day = 0
        # Initialize profit to store the maximum profit achievable
        profit = 0
        # Start sell_day from index 1 since we need to sell after buying
        sell_day = 1

        # Iterate through the array while sell_day is within bounds
        while sell_day < len(prices):
            # If price at buy_day is less than price at sell_day, we can make a profit
            if prices[buy_day] < prices[sell_day]:
                # Update profit if current profit (sell_price - buy_price) is higher
                profit = max(prices[sell_day] - prices[buy_day], profit)
            else:
                # If current price is lower than or equal to buy_day price,
                # update buy_day to current day as it could lead to higher profit later
                buy_day = sell_day
            # Move to the next day for selling
            sell_day += 1
        
        # Return the maximum profit found (0 if no profit is possible)
        return profit