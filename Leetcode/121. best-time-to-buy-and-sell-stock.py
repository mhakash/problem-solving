class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            if(prices[r] < prices[l]):
                l = r
            elif(prices[r] - prices[l] > profit):
                profit = prices[r] - prices[l]
            r += 1

        return profit
