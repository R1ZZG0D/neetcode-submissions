class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, max_profit = 0, 0
        for i in range(len(prices)):            
            for j in range(i+1, len(prices)):
                if (prices[i]>prices[j] or
                prices[i] == prices[j]):                    
                    continue
                #buy = prices[i]
                #sell = prices[j]
                profit = prices[j] - prices[i]
                if max_profit < profit:
                    max_profit = profit
        return max_profit
                
                
