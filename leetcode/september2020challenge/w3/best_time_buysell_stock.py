class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        max_profit = 0
        current_min = prices[0]
        
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            
        return max_profit
