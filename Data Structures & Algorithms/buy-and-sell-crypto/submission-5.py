class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
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
        '''
        '''
        max_profit = 0
        min_buy = prices[0]
        for sell in prices:
            max_profit = max(max_profit, sell - min_buy)
            min_buy = min(min_buy, sell)
        return max_profit
        '''

        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if (prices[l] >= prices[r]):
                l = r                
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            r += 1
        return max_profit

                
