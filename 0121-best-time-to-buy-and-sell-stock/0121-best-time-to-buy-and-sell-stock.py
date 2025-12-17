class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            # update the minimal price
            if price < min_price:
                min_price = price
            # recalculate the profit we could get based on the min price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit