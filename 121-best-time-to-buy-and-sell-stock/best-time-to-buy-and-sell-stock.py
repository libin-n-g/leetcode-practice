class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize buy_day to track the day with lowest price seen so far
        buy_price = prices[0]
        # Initialize profit to store the maximum profit achievable
        profit = 0
        # Iterate through the array while sell_day is within bounds
        for sell_price in prices:
            if buy_price >= sell_price:
                # If current price is lower than or equal to buy_day price,
                # update buy_day to current day as it could lead to higher profit later
                buy_price = sell_price
        
            else:
                # If price at buy_day is less than price at sell_day, we can make a profit
                # Update profit if current profit (sell_price - buy_price) is higher
                profit = max(sell_price - buy_price, profit)

        # Return the maximum profit found (0 if no profit is possible)
        return profit