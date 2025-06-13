class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0
        r = 1
        while l < r < len(prices):
            if prices[l] < prices[r]:
                profit = max(prices[r] - prices[l], profit)
            else:
                l = r
            r += 1
        return profit
        